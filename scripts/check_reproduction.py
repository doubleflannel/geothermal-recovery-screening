#!/usr/bin/env python3
"""Check the regenerated EGS Collab Exp2 worked-example artifacts."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
SUMMARY_PATH = ARTIFACTS / "egs_collab_exp2_summary.json"


EXPECTED = {
    "tau_h": (4.19, 0.03),
    "rmse_c": (0.0125, 0.0005),
    "flow_l_min": (0.400, 0.001),
    "delta_p_mpa": (22.7, 0.1),
    "k_eq_preferred_m2": (1.59e-15, 0.03e-15),
    "k_eq_band_m2_low": (3.52e-16, 0.04e-16),
    "k_eq_band_m2_high": (4.40e-15, 0.04e-15),
}


def require_file(path: Path) -> None:
    if not path.exists():
        raise SystemExit(f"missing required artifact: {path.relative_to(ROOT)}")
    if path.stat().st_size <= 0:
        raise SystemExit(f"empty required artifact: {path.relative_to(ROOT)}")


def check_close(name: str, value: float, expected: float, tolerance: float) -> None:
    if not math.isfinite(value):
        raise SystemExit(f"{name} is not finite: {value}")
    if abs(value - expected) > tolerance:
        raise SystemExit(
            f"{name} out of tolerance: got {value:.12g}, "
            f"expected {expected:.12g} ± {tolerance:.3g}"
        )
    print(f"ok {name}: {value:.12g}")


def main() -> None:
    require_file(ARTIFACTS / "egs_collab_exp2_amu34m_recovery_fit.png")
    require_file(ARTIFACTS / "egs_collab_exp2_amu34m_k_scale_check.png")
    require_file(SUMMARY_PATH)

    summary = json.loads(SUMMARY_PATH.read_text())
    check_close("tau_h", summary["tau_h"], *EXPECTED["tau_h"])
    check_close("rmse_c", summary["rmse_c"], *EXPECTED["rmse_c"])
    check_close("flow_l_min", summary["flow_l_min"], *EXPECTED["flow_l_min"])
    check_close("delta_p_mpa", summary["delta_p_mpa"], *EXPECTED["delta_p_mpa"])
    check_close(
        "k_eq_preferred_m2",
        summary["k_eq_preferred_m2"],
        *EXPECTED["k_eq_preferred_m2"],
    )
    check_close(
        "k_eq_band_m2_low",
        summary["k_eq_band_m2"][0],
        *EXPECTED["k_eq_band_m2_low"],
    )
    check_close(
        "k_eq_band_m2_high",
        summary["k_eq_band_m2"][1],
        *EXPECTED["k_eq_band_m2_high"],
    )

    print("reproduction check passed")


if __name__ == "__main__":
    main()
