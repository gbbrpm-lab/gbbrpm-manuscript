from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
data = pd.read_csv(ROOT / "data" / "scalability.csv")

lower = data["median_ms"] - data["q25_ms"]
upper = data["q75_ms"] - data["median_ms"]

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 10,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
    }
)

fig, ax = plt.subplots(figsize=(6.8, 3.8), constrained_layout=True)
ax.errorbar(
    data["nodes"],
    data["median_ms"],
    yerr=[lower, upper],
    color="#17365d",
    marker="o",
    markersize=4.5,
    linewidth=1.4,
    capsize=3,
    capthick=0.8,
    label="Median with interquartile range",
)
ax.set_xscale("log")
ax.set_xticks(data["nodes"])
ax.set_xticklabels(data["nodes"].astype(str))
ax.set_xlabel("Number of nodes, $|V|$")
ax.set_ylabel("Runtime (ms)")
ax.grid(axis="y", color="#d9d9d9", linewidth=0.6)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, loc="upper left")

figures = ROOT / "figures"
figures.mkdir(exist_ok=True)
fig.savefig(figures / "figure4_8.pdf", bbox_inches="tight")
fig.savefig(figures / "figure4_8.png", dpi=330, bbox_inches="tight")
