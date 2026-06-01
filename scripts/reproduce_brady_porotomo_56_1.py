#!/usr/bin/env python3
"""Reproduce the Brady/PoroTomo 56-1 public threshold-compatible artifacts."""

from __future__ import annotations

import csv
import json
import math
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
ARTIFACTS = ROOT / "artifacts"
DESCRIPTOR_PATH = DATA / "brady_porotomo_56_1_recovery_descriptors.csv"
ALIGNMENT_PATH = DATA / "brady_porotomo_56_1_alignment_summary.json"

MATLAB_BLUE = "#0072BD"
MATLAB_ORANGE = "#D95319"
MATLAB_YELLOW = "#EDB120"
INK = "#111827"
MUTED = "#475569"
GRID = "#e2e8f0"


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def read_descriptors() -> list[dict[str, float | str]]:
    rows: list[dict[str, float | str]] = []
    for row in read_csv_rows(DESCRIPTOR_PATH):
        parsed: dict[str, float | str] = {}
        for key, value in row.items():
            if key in {"band", "column", "fit_type"}:
                parsed[key] = value
            else:
                parsed[key] = float(value)
        rows.append(parsed)
    return rows


def open_interval_descriptor(rows: list[dict[str, float | str]]) -> dict[str, float | str]:
    for row in rows:
        if row["band"] == "350–372 m open interval":
            return row
    raise SystemExit("missing 350-372 m open interval descriptor")


def permeability_sensitivity() -> tuple[list[dict[str, float]], dict[str, float]]:
    slug_volume_m3 = 15.0
    slug_drain_hours = 7.0
    well_radius_m = 0.255
    rho_kg_m3 = 970.0
    gravity = 9.80665
    viscosity_pa_s = [2.0e-4, 3.5e-4, 7.0e-4]
    flow_length_m = [1.0, 5.0, 10.0, 25.0, 50.0]
    outflow_height_m = [10.0, 25.0, 62.0, 120.0, 416.0]
    head_m = [5.0, 15.0, 30.0, 52.0]
    q_m3_s = slug_volume_m3 / (slug_drain_hours * 3600.0)

    rows = []
    for mu, length, height, head in product(
        viscosity_pa_s, flow_length_m, outflow_height_m, head_m
    ):
        area = 2.0 * math.pi * well_radius_m * height
        delta_p = rho_kg_m3 * gravity * head
        rows.append(
            {
                "viscosity_pa_s": mu,
                "flow_length_m": length,
                "outflow_height_m": height,
                "head_m": head,
                "area_m2": area,
                "delta_p_pa": delta_p,
                "q_m3_s": q_m3_s,
                "k_m2": mu * q_m3_s * length / (area * delta_p),
            }
        )

    preferred = [
        row
        for row in rows
        if 2.0e-4 <= row["viscosity_pa_s"] <= 3.5e-4
        and 5.0 <= row["flow_length_m"] <= 25.0
        and 25.0 <= row["outflow_height_m"] <= 120.0
        and 15.0 <= row["head_m"] <= 52.0
    ]
    central = [
        row
        for row in rows
        if row["viscosity_pa_s"] == 3.5e-4
        and row["flow_length_m"] == 10.0
        and row["outflow_height_m"] == 62.0
        and row["head_m"] == 30.0
    ][0]

    values = [row["k_m2"] for row in rows]
    preferred_values = [row["k_m2"] for row in preferred]
    summary = {
        "slug_volume_m3": slug_volume_m3,
        "slug_drain_hours": slug_drain_hours,
        "well_radius_m": well_radius_m,
        "full_min_m2": min(values),
        "full_median_m2": float(np.median(values)),
        "full_max_m2": max(values),
        "preferred_min_m2": min(preferred_values),
        "preferred_median_m2": float(np.median(preferred_values)),
        "preferred_max_m2": max(preferred_values),
        "central_m2": central["k_m2"],
    }
    return rows, summary


def fmt_m2(value: float) -> str:
    return f"{value:.2e} m²"


def plot_slug_bridge(
    descriptors: list[dict[str, float | str]],
    sensitivity_rows: list[dict[str, float]],
    bridge: dict[str, float],
) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    fig, axes = plt.subplots(2, 1, figsize=(11.2, 8.4), gridspec_kw={"height_ratios": [1.0, 1.25]})
    fig.subplots_adjust(left=0.23, right=0.96, top=0.88, bottom=0.11, hspace=0.42)
    fig.suptitle(
        "Brady/PoroTomo 56-1 public reproduction",
        fontsize=17,
        fontweight="bold",
        color=INK,
        x=0.14,
        ha="left",
    )
    fig.text(
        0.14,
        0.915,
        "Processed public-source snippets reproduce the recovery descriptor and slug-drainage bridge.",
        fontsize=10.5,
        color=MUTED,
    )

    ax = axes[0]
    bands = [str(row["band"]) for row in descriptors]
    tau = [float(row["tau_h"]) for row in descriptors]
    colors = [MATLAB_ORANGE, MATLAB_BLUE, "#7E2F8E"]
    y = np.arange(len(bands))
    ax.barh(y, tau, color=colors, alpha=0.88)
    ax.set_yticks(y)
    ax.set_yticklabels(bands)
    ax.invert_yaxis()
    ax.set_xlabel("Fitted recovery descriptor tau (h)")
    ax.set_title("Temperature-recovery descriptors", loc="left", fontsize=12)
    ax.grid(True, axis="x", color=GRID)
    for idx, value in enumerate(tau):
        ax.text(value + 2, idx, f"{value:.1f} h", va="center", fontsize=9, color=INK)

    ax = axes[1]
    rows = [
        ("Full sensitivity", bridge["full_min_m2"], bridge["full_median_m2"], bridge["full_max_m2"], MUTED),
        (
            "Preferred range",
            bridge["preferred_min_m2"],
            bridge["central_m2"],
            bridge["preferred_max_m2"],
            MATLAB_ORANGE,
        ),
        ("Patterson context", 2.24e-14, 4.43e-14, 6.62e-14, MATLAB_BLUE),
    ]
    y = np.arange(len(rows))
    for idx, (label, low, center, high, color) in enumerate(rows):
        plot_high = min(high, 1.0e-12)
        ax.plot([low, plot_high], [idx, idx], color=color, linewidth=8, solid_capstyle="round")
        ax.scatter([center], [idx], s=110, color=MATLAB_YELLOW, edgecolor=INK, zorder=4)
        if high / low < 10:
            ax.text(
                math.sqrt(low * plot_high),
                idx + 0.18,
                f"{fmt_m2(low)} to {fmt_m2(high)}",
                ha="center",
                fontsize=8.5,
                color=MUTED,
            )
        else:
            ax.text(low, idx + 0.18, fmt_m2(low), ha="left", fontsize=8.5, color=MUTED)
            high_label = f"extends to {fmt_m2(high)}" if high > 1.0e-12 else fmt_m2(high)
            ax.text(plot_high, idx + 0.18, high_label, ha="right", fontsize=8.5, color=MUTED)
    ax.axvline(1.0e-14, color=INK, linestyle=":", linewidth=1.6, alpha=0.75)
    ax.text(1.08e-14, -0.38, "1e-14 method-effectiveness threshold", fontsize=8.8, color=INK)
    ax.set_xscale("log")
    ax.set_xlim(1.0e-16, 1.0e-12)
    ax.set_yticks(y)
    ax.set_yticklabels([row[0] for row in rows])
    ax.invert_yaxis()
    ax.set_xlabel("Bulk/model-equivalent permeability (m²)")
    ax.set_title("Slug-drainage permeability bridge", loc="left", fontsize=12)
    ax.grid(True, axis="x", which="both", color=GRID)

    fig.savefig(ARTIFACTS / "brady_porotomo_56_1_slug_bridge.png", dpi=180)
    plt.close(fig)


def main() -> None:
    descriptors = read_descriptors()
    open_interval = open_interval_descriptor(descriptors)
    alignment = json.loads(ALIGNMENT_PATH.read_text())
    sensitivity_rows, bridge = permeability_sensitivity()
    plot_slug_bridge(descriptors, sensitivity_rows, bridge)

    summary = {
        "case": "brady_porotomo_56_1",
        "status": "qualified_threshold_compatible_public_data_route",
        "open_interval_tau_h": open_interval["tau_h"],
        "open_interval_rmse_c": open_interval["rmse_C"],
        "dts_window_utc": [alignment["dts_start_utc"], alignment["dts_end_utc"]],
        "slug_volume_m3": bridge["slug_volume_m3"],
        "slug_drain_hours": bridge["slug_drain_hours"],
        "k_eq_central_m2": bridge["central_m2"],
        "k_eq_preferred_range_m2": [
            bridge["preferred_min_m2"],
            bridge["preferred_max_m2"],
        ],
        "k_eq_full_range_m2": [bridge["full_min_m2"], bridge["full_max_m2"]],
        "independent_comparison_context_m2": [2.24e-14, 6.62e-14],
        "comparison_tier": "same-field/fault-scale same-order support",
        "claim_boundary": (
            "bulk/model-equivalent slug-drainage estimate; not measured rock "
            "permeability, exact fracture permeability, or exact outflow-patch validation"
        ),
    }
    ARTIFACTS.mkdir(exist_ok=True)
    (ARTIFACTS / "brady_porotomo_56_1_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )

    print(f"open_interval_tau_h = {float(summary['open_interval_tau_h']):.2f}")
    print(f"open_interval_rmse_c = {float(summary['open_interval_rmse_c']):.3f}")
    print(f"k_eq_central_m2 = {summary['k_eq_central_m2']:.3e}")
    print(
        "k_eq_preferred_range_m2 = "
        f"{summary['k_eq_preferred_range_m2'][0]:.3e}-"
        f"{summary['k_eq_preferred_range_m2'][1]:.3e}"
    )


if __name__ == "__main__":
    main()
