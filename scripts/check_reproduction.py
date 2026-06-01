#!/usr/bin/env python3
"""Check regenerated public thermal-recovery screening artifacts."""

from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
BRADY_SUMMARY_PATH = ARTIFACTS / "brady_porotomo_56_1_summary.json"


BRADY_EXPECTED = {
    "open_interval_tau_h": (118.08, 0.05),
    "open_interval_rmse_c": (0.472, 0.005),
    "k_eq_central_m2": (7.35e-14, 0.03e-14),
    "k_eq_preferred_range_m2_low": (6.26e-15, 0.04e-15),
    "k_eq_preferred_range_m2_high": (9.11e-13, 0.04e-13),
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


def check_brady() -> None:
    require_file(ARTIFACTS / "brady_porotomo_56_1_dts_alignment.png")
    require_file(ARTIFACTS / "brady_porotomo_56_1_slug_bridge.png")
    require_file(BRADY_SUMMARY_PATH)

    summary = json.loads(BRADY_SUMMARY_PATH.read_text())
    check_close(
        "brady_open_interval_tau_h",
        summary["open_interval_tau_h"],
        *BRADY_EXPECTED["open_interval_tau_h"],
    )
    check_close(
        "brady_open_interval_rmse_c",
        summary["open_interval_rmse_c"],
        *BRADY_EXPECTED["open_interval_rmse_c"],
    )
    check_close(
        "brady_k_eq_central_m2",
        summary["k_eq_central_m2"],
        *BRADY_EXPECTED["k_eq_central_m2"],
    )
    check_close(
        "brady_k_eq_preferred_range_m2_low",
        summary["k_eq_preferred_range_m2"][0],
        *BRADY_EXPECTED["k_eq_preferred_range_m2_low"],
    )
    check_close(
        "brady_k_eq_preferred_range_m2_high",
        summary["k_eq_preferred_range_m2"][1],
        *BRADY_EXPECTED["k_eq_preferred_range_m2_high"],
    )


def main() -> None:
    check_brady()
    print("reproduction check passed")


if __name__ == "__main__":
    main()
