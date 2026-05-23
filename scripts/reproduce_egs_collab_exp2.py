#!/usr/bin/env python3
"""Reproduce the EGS Collab Exp2 AMU 34 m worked-example artifacts."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "processed"
ARTIFACTS = ROOT / "artifacts"


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def fit_exponential(elapsed_h: np.ndarray, delta_c: np.ndarray) -> dict[str, float]:
    def solve_for_tau(tau_h: float) -> tuple[float, float, float]:
        shape = np.exp(-elapsed_h / tau_h)
        design = np.column_stack([np.ones_like(shape), shape])
        baseline, amplitude = np.linalg.lstsq(design, delta_c, rcond=None)[0]
        fitted = baseline + amplitude * shape
        rmse = float(np.sqrt(np.mean((delta_c - fitted) ** 2)))
        return float(baseline), float(amplitude), rmse

    low = 0.2
    high = 40.0
    phi = (1 + math.sqrt(5)) / 2
    for _ in range(90):
        left = high - (high - low) / phi
        right = low + (high - low) / phi
        if solve_for_tau(left)[2] < solve_for_tau(right)[2]:
            high = right
        else:
            low = left

    tau_h = (low + high) / 2
    baseline, amplitude, rmse = solve_for_tau(tau_h)
    fitted = baseline + amplitude * np.exp(-elapsed_h / tau_h)
    return {
        "tau_h": float(tau_h),
        "baseline_c": baseline,
        "amplitude_c": amplitude,
        "rmse_c": rmse,
        "fitted_delta_c": fitted.tolist(),
    }


def read_boundary_values() -> dict[str, float]:
    rows = read_csv_rows(DATA / "egs_collab_exp2_boundary_inputs.csv")
    return {row["name"]: float(row["value"]) for row in rows}


def model_equivalent_k(boundary: dict[str, float]) -> dict[str, float]:
    flow_m3_s = boundary["flow_l_min_pre_stop_median"] / 1000.0 / 60.0
    delta_pressure_pa = boundary["delta_pressure_mpa"] * 1_000_000.0
    mu = boundary["water_viscosity"]

    def calc(length_m: float, area_m2: float) -> float:
        return mu * flow_m3_s * length_m / (area_m2 * delta_pressure_pa)

    return {
        "preferred_m2": calc(
            boundary["path_length_preferred"], boundary["contact_area_preferred"]
        ),
        "low_m2": calc(boundary["path_length_low"], boundary["contact_area_high"]),
        "high_m2": calc(boundary["path_length_high"], boundary["contact_area_low"]),
    }


def plot_recovery(elapsed_h: np.ndarray, delta_c: np.ndarray, fit: dict[str, float]) -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.scatter(elapsed_h, delta_c, s=32, color="#2563eb", alpha=0.78, label="Measured recovery")
    ax.plot(
        elapsed_h,
        fit["fitted_delta_c"],
        color="#dc2626",
        linewidth=3.0,
        label=f"Exponential descriptor: tau = {fit['tau_h']:.2f} h",
    )
    ax.axhline(0, color="#475569", linewidth=1.0, alpha=0.5)
    ax.set_title("EGS Collab Exp2 AMU 34 m thermal recovery")
    ax.set_xlabel("Hours after pump stop")
    ax.set_ylabel("Temperature anomaly (°C)")
    ax.grid(True, which="major", color="#e2e8f0", linewidth=1.0)
    ax.legend(loc="upper right", frameon=True)
    fig.tight_layout()
    fig.savefig(ARTIFACTS / "egs_collab_exp2_amu34m_recovery_fit.png", dpi=180)
    plt.close(fig)


def plot_permeability(k: dict[str, float], comparison_rows: list[dict[str, str]]) -> None:
    labels = ["This worked example"]
    lows = [k["low_m2"]]
    highs = [k["high_m2"]]
    centers = [k["preferred_m2"]]
    colors = ["#2563eb"]

    for row in comparison_rows:
        if row["category"] == "our model-equivalent result":
            continue
        labels.append(row["label"].split(" — ")[0])
        lows.append(float(row["min_m2"]))
        highs.append(float(row["max_m2"]))
        centers.append(float("nan") if row["central_m2"] == "" else float(row["central_m2"]))
        colors.append("#16a34a")

    y = np.arange(len(labels))
    fig, ax = plt.subplots(figsize=(9, 5.2))
    for idx, (low, high, center, color) in enumerate(zip(lows, highs, centers, colors)):
        ax.plot([low, high], [idx, idx], color=color, linewidth=8, solid_capstyle="round")
        if math.isfinite(center):
            ax.scatter([center], [idx], s=110, color="#111827", zorder=3, label="Preferred value" if idx == 0 else None)

    ax.set_xscale("log")
    ax.set_xlim(1e-18, 1e-12)
    ax.set_yticks(y)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_xlabel("Permeability (m²)")
    ax.set_title("Bulk/model-equivalent permeability scale check")
    ax.grid(True, axis="x", which="both", color="#e2e8f0", linewidth=1.0)
    ax.text(
        1.1e-18,
        len(labels) - 0.15,
        "Blue = public-data worked example; green = published EGS Collab comparison ranges.",
        fontsize=10,
        color="#334155",
    )
    fig.tight_layout()
    fig.savefig(ARTIFACTS / "egs_collab_exp2_amu34m_k_scale_check.png", dpi=180)
    plt.close(fig)


def main() -> None:
    recovery_rows = read_csv_rows(DATA / "egs_collab_exp2_amu34m_recovery.csv")
    elapsed_h = np.array([float(row["elapsed_h"]) for row in recovery_rows])
    delta_c = np.array([float(row["temperature_delta_c"]) for row in recovery_rows])
    fit = fit_exponential(elapsed_h, delta_c)

    boundary = read_boundary_values()
    k = model_equivalent_k(boundary)
    comparison_rows = read_csv_rows(DATA / "egs_collab_exp2_published_k_ranges.csv")

    plot_recovery(elapsed_h, delta_c, fit)
    plot_permeability(k, comparison_rows)

    summary = {
        "case": "egs_collab_exp2_amu34m",
        "recovery_rows": len(recovery_rows),
        "tau_h": fit["tau_h"],
        "rmse_c": fit["rmse_c"],
        "flow_l_min": boundary["flow_l_min_pre_stop_median"],
        "delta_p_mpa": boundary["delta_pressure_mpa"],
        "k_eq_preferred_m2": k["preferred_m2"],
        "k_eq_band_m2": [k["low_m2"], k["high_m2"]],
        "claim_boundary": "bulk/model-equivalent scale check only; not measured rock permeability",
    }
    ARTIFACTS.mkdir(exist_ok=True)
    (ARTIFACTS / "egs_collab_exp2_summary.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )

    print(f"tau_h = {summary['tau_h']:.3f}")
    print(f"rmse_c = {summary['rmse_c']:.5f}")
    print(f"flow_l_min = {summary['flow_l_min']:.3f}")
    print(f"deltaP_mpa = {summary['delta_p_mpa']:.1f}")
    print(f"k_eq_preferred_m2 = {summary['k_eq_preferred_m2']:.3e}")
    print(
        "k_eq_band_m2 = "
        f"{summary['k_eq_band_m2'][0]:.3e}–{summary['k_eq_band_m2'][1]:.3e}"
    )


if __name__ == "__main__":
    main()
