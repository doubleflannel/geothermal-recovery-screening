#!/usr/bin/env python3
"""Reproduce the Brady/PoroTomo 56-1 public threshold-compatible artifacts."""

from __future__ import annotations

import csv
import json
import math
import textwrap
from itertools import product
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
ARTIFACTS = ROOT / "artifacts"
DESCRIPTOR_PATH = DATA / "brady_porotomo_56_1_recovery_descriptors.csv"
ALIGNMENT_PATH = DATA / "brady_porotomo_56_1_alignment_summary.json"
CURVE_PATH = DATA / "brady_porotomo_56_1_recovery_fit_curve.csv"

INK = "#111827"
MUTED = "#4b5563"
GRID = "#e5e7eb"
BLUE = "#2563eb"
ORANGE = "#d97706"
TEAL = "#0f766e"
GRAY = "#64748b"
RED = "#dc2626"
YELLOW = "#fbbf24"
PAPER = "#ffffff"
BG = "#f8fafc"
THRESHOLD_M2 = 1.0e-14


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def parse_numeric_rows(path: Path, text_columns: set[str] | None = None) -> list[dict[str, float | str]]:
    text_columns = text_columns or set()
    rows: list[dict[str, float | str]] = []
    for row in read_csv_rows(path):
        parsed: dict[str, float | str] = {}
        for key, value in row.items():
            if key in text_columns:
                parsed[key] = value
            else:
                parsed[key] = float(value)
        rows.append(parsed)
    return rows


def read_descriptors() -> list[dict[str, float | str]]:
    return parse_numeric_rows(DESCRIPTOR_PATH, {"band", "column", "fit_type"})


def read_fit_curve() -> list[dict[str, float | str]]:
    return parse_numeric_rows(CURVE_PATH, {"time_utc"})


def open_interval_descriptor(rows: list[dict[str, float | str]]) -> dict[str, float | str]:
    for row in rows:
        if row["band"] == "350-372 m open interval" or row["band"] == "350–372 m open interval":
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


def fmt_power_m2(value: float) -> str:
    exponent = int(math.floor(math.log10(abs(value))))
    coefficient = value / 10**exponent
    if 1.0 <= coefficient < 9.995:
        return rf"${coefficient:.2f}\times10^{{{exponent}}}$ m²"
    exponent += 1
    coefficient = value / 10**exponent
    return rf"${coefficient:.2f}\times10^{{{exponent}}}$ m²"


def clean_label(text: object) -> str:
    return str(text).replace("–", "-")


def style_axes(ax: plt.Axes, grid_axis: str = "x") -> None:
    ax.set_facecolor(PAPER)
    ax.grid(True, axis=grid_axis, which="both", color=GRID, alpha=0.9)
    for spine in ["top", "right", "left"]:
        ax.spines[spine].set_visible(False)
    ax.tick_params(axis="y", length=0)


def add_card(fig: plt.Figure, xywh: tuple[float, float, float, float], title: str, body: str, color: str) -> None:
    ax = fig.add_axes(xywh)
    ax.set_axis_off()
    rect = plt.Rectangle((0, 0), 1, 1, transform=ax.transAxes, facecolor=PAPER, edgecolor=GRID, linewidth=1.2)
    ax.add_patch(rect)
    ax.add_patch(plt.Rectangle((0, 0), 0.018, 1, transform=ax.transAxes, facecolor=color, edgecolor=color))
    wrapped = "\n".join(textwrap.wrap(body, width=54, break_long_words=False))
    ax.text(0.055, 0.78, title, transform=ax.transAxes, fontsize=12, fontweight="bold", color=INK, va="top")
    ax.text(0.055, 0.50, wrapped, transform=ax.transAxes, fontsize=9.2, color=MUTED, va="top", linespacing=1.35)


def plot_dts_alignment(
    descriptors: list[dict[str, float | str]],
    alignment: dict[str, object],
    fit_curve: list[dict[str, float | str]],
) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(13.2, 8.6))
    fig.patch.set_facecolor(BG)
    fig.subplots_adjust(left=0.13, right=0.97, top=0.80, bottom=0.13)
    fig.text(0.04, 0.93, "Brady/PoroTomo 56-1 temperature recovery", fontsize=19, fontweight="bold", color=INK)
    fig.text(
        0.04,
        0.885,
        "Public-source-derived hourly temperature points and fitted recovery curve for the 350-372 m open interval used in Ivan's bridge analysis.",
        fontsize=11,
        color=MUTED,
    )

    x = np.array([float(row["hours_since_dts_start"]) for row in fit_curve])
    y = np.array([float(row["open_interval_350_372m_C"]) for row in fit_curve])
    y_fit = np.array([float(row["open_interval_350_372m_fit_C"]) for row in fit_curve])
    open_desc = open_interval_descriptor(descriptors)
    mask = x >= 0
    x = x[mask]
    y = y[mask]
    y_fit = y_fit[mask]

    ax.scatter(x, y, s=28, color=BLUE, alpha=0.78, label="Hourly temperature points")
    ax.plot(x, y_fit, color=ORANGE, linewidth=3.0, label="Fitted recovery curve")
    ax.set_xlabel("Hours since DTS recovery-window start", fontsize=11)
    ax.set_ylabel("Open-interval temperature (°C)", fontsize=11)
    ax.set_title("Temperature recovery data and fit", loc="left", fontsize=13, fontweight="bold", pad=12)
    ax.legend(loc="lower right", frameon=True, facecolor="white", edgecolor=GRID)
    style_axes(ax, "both")
    ax.set_xlim(0, max(x) * 1.02)
    ax.set_ylim(min(y.min(), y_fit.min()) - 0.4, max(y.max(), y_fit.max()) + 0.4)
    ax.text(
        0.02,
        0.93,
        f"tau = {float(open_desc['tau_h']):.2f} h\nRMSE = {float(open_desc['rmse_C']):.3f} °C",
        transform=ax.transAxes,
        fontsize=10,
        color=INK,
        va="top",
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": GRID},
    )
    fig.savefig(ARTIFACTS / "brady_porotomo_56_1_dts_alignment.png", dpi=180)
    plt.close(fig)

def plot_slug_bridge(bridge: dict[str, float]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(13.2, 8.6))
    fig.patch.set_facecolor(BG)
    fig.subplots_adjust(left=0.19, right=0.97, top=0.76, bottom=0.17)
    fig.text(0.04, 0.93, "Brady/PoroTomo 56-1 thermal-recovery permeability bridge", fontsize=19, fontweight="bold", color=INK)
    fig.text(
        0.04,
        0.885,
        "Blue/gray = Ivan analysis from Brady temperature recovery. Teal = independent published pressure-model context from Patterson (2018).",
        fontsize=11,
        color=MUTED,
    )

    rows = [
        ("Ivan: Brady bridge", bridge["preferred_min_m2"], bridge["central_m2"], bridge["preferred_max_m2"], BLUE),
        ("Ivan: full sensitivity", bridge["full_min_m2"], bridge["full_median_m2"], bridge["full_max_m2"], GRAY),
        ("Patterson (2018) reference", 2.24e-14, 4.43e-14, 6.62e-14, TEAL),
    ]
    y = np.arange(len(rows))[::-1]
    for yi, (label, low, center, high, color) in zip(y, rows):
        plot_high = min(high, 1.0e-10)
        ax.plot([low, plot_high], [yi, yi], color=color, linewidth=9, solid_capstyle="round", alpha=0.88)
        ax.scatter([low, plot_high], [yi, yi], color=color, s=68, zorder=3)
        ax.scatter([center], [yi], marker="*", s=240, color=YELLOW, edgecolor=INK, linewidth=1.0, zorder=4)
        value_y_offset = 0.25 if yi == 0 else -0.25
        value_va = "bottom" if yi == 0 else "top"
        ax.text(low, yi + value_y_offset, fmt_power_m2(low), ha="left", va=value_va, fontsize=9, color=MUTED)
        high_label = f"extends to {fmt_power_m2(high)}" if high > 1.0e-10 else fmt_power_m2(high)
        ax.text(plot_high, yi + value_y_offset, high_label, ha="right", va=value_va, fontsize=9, color=MUTED)
        ax.text(
            center,
            yi + 0.25,
            f"central {fmt_power_m2(center)}",
            ha="center",
            va="bottom",
            fontsize=9,
            color=INK,
            bbox={"boxstyle": "round,pad=0.20", "facecolor": "white", "edgecolor": GRID},
        )

    ax.axvline(THRESHOLD_M2, color=INK, linewidth=2.0, linestyle="--", alpha=0.75)
    ax.text(
        THRESHOLD_M2,
        max(y) + 0.48,
        "$10^{-14}$ m²\nmethod-effective range",
        fontsize=9.5,
        color=INK,
        ha="center",
        va="top",
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": GRID},
    )
    ax.set_xscale("log")
    ax.set_xlim(1e-16, 1e-10)
    ax.set_ylim(-0.45, max(y) + 0.55)
    ax.set_yticks(y)
    ax.set_yticklabels([row[0] for row in rows], fontsize=10)
    ax.set_xlabel("Model-equivalent permeability scale (m², log scale)", fontsize=11)
    ax.set_title("Analysis ranges versus published reference", loc="left", fontsize=13, fontweight="bold", pad=12)
    style_axes(ax)
    fig.savefig(ARTIFACTS / "brady_porotomo_56_1_slug_bridge.png", dpi=180)
    fig.savefig(ARTIFACTS / "brady_porotomo_56_1_thermal_recovery_bridge.png", dpi=180)
    plt.close(fig)


def main() -> None:
    descriptors = read_descriptors()
    fit_curve = read_fit_curve()
    open_interval = open_interval_descriptor(descriptors)
    alignment = json.loads(ALIGNMENT_PATH.read_text())
    _sensitivity_rows, bridge = permeability_sensitivity()
    plot_dts_alignment(descriptors, alignment, fit_curve)
    plot_slug_bridge(bridge)

    summary = {
        "case": "brady_porotomo_56_1",
        "status": "qualified_threshold_compatible_public_data_route",
        "pf_2026_label": "P/F-core or near-core threshold-compatible",
        "open_interval_tau_h": open_interval["tau_h"],
        "open_interval_rmse_c": open_interval["rmse_C"],
        "dts_window_utc": [alignment["dts_start_utc"], alignment["dts_end_utc"]],
        "slug_volume_m3": bridge["slug_volume_m3"],
        "slug_drain_hours": bridge["slug_drain_hours"],
        "k_eq_central_m2": bridge["central_m2"],
        "k_eq_preferred_range_m2": [bridge["preferred_min_m2"], bridge["preferred_max_m2"]],
        "k_eq_full_range_m2": [bridge["full_min_m2"], bridge["full_max_m2"]],
        "independent_comparison_context_m2": [2.24e-14, 6.62e-14],
        "comparison_tier": "same-field/fault-scale same-order support",
        "dominant_uncertainty": "effective outflow geometry, especially L/A; excess head is secondary",
        "claim_boundary": (
            "bulk/model-equivalent slug-drainage estimate; not measured rock "
            "permeability, exact fracture permeability, or exact outflow-patch validation"
        ),
    }
    ARTIFACTS.mkdir(exist_ok=True)
    (ARTIFACTS / "brady_porotomo_56_1_summary.json").write_text(json.dumps(summary, indent=2) + "\n")

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
