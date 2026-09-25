from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA = pd.read_csv(ROOT / "data" / "core_scenarios.csv")
FIGURES = ROOT / "figures"
FIGURES.mkdir(exist_ok=True)

NETWORKS = ["N1", "N2", "N3", "N4", "N5"]
COLORS = {
    "N1": "#17365d",
    "N2": "#b24a3b",
    "N3": "#6f8f3d",
    "N4": "#76538d",
    "N5": "#2f8fa8",
}
MARKERS = {"N1": "o", "N2": "s", "N3": "^", "N4": "D", "N5": "v"}

plt.rcParams.update(
    {
        "font.family": "serif",
        "font.size": 9,
        "axes.labelsize": 9,
        "axes.titlesize": 9,
        "xtick.labelsize": 8,
        "ytick.labelsize": 8,
        "legend.fontsize": 8,
    }
)


def save_jpg(fig, name):
    fig.savefig(
        FIGURES / name,
        dpi=330,
        bbox_inches="tight",
        facecolor="white",
        pil_kwargs={"quality": 95},
    )
    plt.close(fig)


def style_axis(ax):
    ax.grid(axis="y", color="#d9d9d9", linewidth=0.6)
    ax.spines[["top", "right"]].set_visible(False)


def figure_4_2():
    subset = DATA[DATA["scenario_family"] == "severity"].copy()
    subset["parameter"] = pd.to_numeric(subset["parameter"])

    fig, ax = plt.subplots(figsize=(6.8, 3.8), constrained_layout=True)
    for network in NETWORKS:
        rows = subset[subset["network"] == network].sort_values("parameter")
        ax.plot(
            rows["parameter"], rows["outlet_risk"], label=network,
            color=COLORS[network], marker=MARKERS[network],
            markersize=4.5, linewidth=1.4,
        )
    ax.set_xlabel("Source disturbance severity, $B$")
    ax.set_ylabel("Outlet risk index, $R$")
    ax.set_xticks([0.25, 0.50, 0.75, 1.00])
    ax.set_ylim(0, 0.80)
    style_axis(ax)
    ax.legend(title="Network", ncol=5, frameon=False, loc="upper left")
    save_jpg(fig, "figure4_2.jpg")


def figure_4_3():
    subset = DATA[DATA["scenario_family"] == "lc_stress"].copy()
    subset["parameter"] = pd.to_numeric(subset["parameter"])

    fig, ax = plt.subplots(figsize=(6.8, 3.8), constrained_layout=True)
    for network in NETWORKS:
        rows = subset[subset["network"] == network].sort_values("parameter")
        ax.plot(
            rows["parameter"], rows["outlet_risk"], label=network,
            color=COLORS[network], marker=MARKERS[network],
            markersize=4.5, linewidth=1.4,
        )
    ax.set_xlabel("Load scale applied before $S=\\min(1,L/C)$")
    ax.set_ylabel("Outlet risk index, $R$")
    ax.set_xticks([0.50, 0.75, 1.00, 1.25, 1.50])
    ax.set_ylim(0, 1.05)
    style_axis(ax)
    ax.legend(title="Network", ncol=5, frameon=False, loc="upper left")
    save_jpg(fig, "figure4_3.jpg")


def figure_4_4():
    subset = DATA[DATA["scenario_family"] == "blockage_location"].copy()
    fig = plt.figure(figsize=(6.8, 4.8), constrained_layout=True)
    grid = fig.add_gridspec(2, 3)
    axes = [
        fig.add_subplot(grid[0, 0]),
        fig.add_subplot(grid[0, 1]),
        fig.add_subplot(grid[0, 2]),
        fig.add_subplot(grid[1, 0]),
        fig.add_subplot(grid[1, 1:]),
    ]
    for ax, network in zip(axes, NETWORKS):
        rows = subset[subset["network"] == network]
        x = range(len(rows))
        ax.bar(x, rows["outlet_risk"], color=COLORS[network], width=0.70)
        ax.set_title(network, fontweight="bold")
        ax.set_xticks(list(x))
        ax.set_xticklabels(rows["location"].astype(str))
        ax.set_ylim(0, 0.80)
        style_axis(ax)
    axes[0].set_ylabel("Outlet risk, $R$")
    axes[3].set_ylabel("Outlet risk, $R$")
    axes[3].set_xlabel("Tested disturbance location")
    axes[4].set_xlabel("Tested disturbance location")
    save_jpg(fig, "figure4_4.jpg")


def figure_4_5():
    subset = DATA[DATA["scenario_family"] == "source_combination"].copy()
    fig, axes = plt.subplots(
        1, 2, figsize=(6.8, 3.8), sharey=True, constrained_layout=True
    )
    for ax, network in zip(axes, ["N3", "N5"]):
        rows = subset[subset["network"] == network]
        x = range(len(rows))
        bars = ax.bar(x, rows["outlet_risk"], color=COLORS[network], width=0.68)
        ax.set_title(f"Network {network}", fontweight="bold")
        ax.set_xticks(list(x))
        ax.set_xticklabels(
            rows["parameter"].astype(str),
            rotation=35 if network == "N5" else 0,
            ha="right" if network == "N5" else "center",
        )
        ax.set_xlabel("Active multi-source configuration")
        ax.set_ylim(0, 0.80)
        style_axis(ax)
        ax.bar_label(bars, fmt="%.4f", padding=2, fontsize=7)
    axes[0].set_ylabel("Outlet risk index, $R$")
    save_jpg(fig, "figure4_5.jpg")


if __name__ == "__main__":
    figure_4_2()
    figure_4_3()
    figure_4_4()
    figure_4_5()
