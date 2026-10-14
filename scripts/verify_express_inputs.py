"""Verify the preserved Express inputs without running benchmark experiments."""

import csv
import hashlib
import json
from collections import defaultdict, deque
from pathlib import Path


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify():
    root = Path(__file__).resolve().parents[1]
    case = root / "data/software/express_4.18.2"
    historical = json.loads(
        (root / "results/paper/paper_outputs_manifest.json").read_text()
    )["input_sha256"]
    expected = {name.replace("\\", "/"): value for name, value in historical.items()}
    manifest = json.loads((case / "manifest.json").read_text())
    digests = {}
    for name in ("nodes.csv", "edges.csv", "deps_dev_dependencies.json", "osv_snapshot.json"):
        digests[name] = hashlib.sha256((case / name).read_bytes()).hexdigest()
    for name in ("nodes.csv", "edges.csv"):
        require(digests[name] == expected[f"data/software/express_4.18.2/{name}"],
                f"Historical CSV hash mismatch: {name}")
    require(digests["deps_dev_dependencies.json"] == manifest["dependency_snapshot_sha256"],
            "Dependency snapshot hash mismatch")
    require(digests["osv_snapshot.json"] == manifest["osv_snapshot_sha256"],
            "OSV snapshot hash mismatch")
    with (case / "nodes.csv").open(newline="", encoding="utf-8-sig") as stream:
        nodes = list(csv.DictReader(stream))
    with (case / "edges.csv").open(newline="", encoding="utf-8-sig") as stream:
        edges = list(csv.DictReader(stream))
    dependency = json.loads((case / "deps_dev_dependencies.json").read_text())
    osv = json.loads((case / "osv_snapshot.json").read_text())
    require(len(nodes) == manifest["node_count"] == 71, "Node inventory mismatch")
    require(len(edges) == manifest["edge_count"] == 128, "Edge inventory mismatch")
    require(len(dependency["nodes"]) == len(nodes), "Dependency node count mismatch")
    require(len(dependency["edges"]) == len(edges), "Dependency edge count mismatch")
    require(not dependency.get("error"), "Dependency response reports an error")
    require(len(osv["exact_version_results"]) == len(nodes), "OSV result count mismatch")
    identities = {node["node"] for node in nodes}
    require(len(identities) == len(nodes), "Duplicate node identity")
    by_index = {int(node["deps_dev_index"]): node for node in nodes}
    require(set(by_index) == set(range(len(nodes))), "Invalid dependency indices")
    positive = []
    for index, source in enumerate(dependency["nodes"]):
        node = by_index[index]
        key = source["versionKey"]
        require(node["node"] == f"npm:{key['name']}@{key['version']}", "Package identity mismatch")
        require(node["relation_to_root"] == source["relation"], "Package relation mismatch")
        identifiers = {item["id"] for item in osv["exact_version_results"][index].get("vulns", [])}
        csv_identifiers = set(filter(None, node["advisory_ids"].split("|")))
        require(identifiers == csv_identifiers, f"Advisory identity mismatch: {node['node']}")
        require(int(node["advisory_count"]) == len(identifiers), "Advisory count mismatch")
        require(0 <= float(node["B"]) <= 1, "Local disturbance outside [0,1]")
        if float(node["B"]) > 0:
            require(bool(identifiers), "Positive local input lacks an advisory record")
            positive.append(node["node"])
    expected_origins = {
        "npm:express@4.18.2", "npm:body-parser@1.20.1", "npm:path-to-regexp@0.1.7",
        "npm:qs@6.11.0", "npm:cookie@0.5.0", "npm:send@0.18.0", "npm:serve-static@1.15.0",
    }
    require(set(positive) == expected_origins, "Seven historical advisory origins do not match")
    incoming = dict.fromkeys(identities, 0)
    children = defaultdict(list)
    resolved = set()
    for edge in edges:
        require(edge["source"] in identities and edge["target"] in identities, "Unknown edge endpoint")
        dependent = int(edge["deps_dev_dependent_index"])
        dependency_index = int(edge["deps_dev_dependency_index"])
        require(edge["source"] == by_index[dependency_index]["node"] and
                edge["target"] == by_index[dependent]["node"], "Edge direction mismatch")
        for field in ("S", "tau"):
            require(0 <= float(edge[field]) <= 1, f"Edge {field} outside [0,1]")
        resolved.add((dependent, dependency_index, edge["requirement"]))
        children[edge["source"]].append(edge["target"])
        incoming[edge["target"]] += 1
    source_edges = {(edge["fromNode"], edge["toNode"], edge["requirement"])
                    for edge in dependency["edges"]}
    require(resolved == source_edges and len(resolved) == len(edges), "Dependency edge inventory mismatch")
    queue = deque(node for node, count in incoming.items() if count == 0)
    ordered = []
    while queue:
        node = queue.popleft()
        ordered.append(node)
        for target in children[node]:
            incoming[target] -= 1
            if incoming[target] == 0:
                queue.append(target)
    require(len(ordered) == len(nodes), "Dependency graph contains a cycle")
    return {
        "case_id": manifest["case_id"],
        "node_count": len(nodes), "edge_count": len(edges), "dag": True,
        "edge_direction": "dependency_to_dependent",
        "historical_csv_hashes_match": True,
        "source_snapshot_hashes_match": True,
        "advisory_origin_count": len(positive), "advisory_origins": sorted(positive),
        "sha256": digests,
        "verification_scope": "Input identity, graph integrity, and advisory-origin consistency only.",
        "stochastic_benchmark_executed": False,
        "independent_incident_validation": False,
    }


if __name__ == "__main__":
    print(json.dumps(verify(), indent=2, sort_keys=True))
