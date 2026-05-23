# EGS Collab Exp2 AMU 34 m worked example

This page documents the single reproducible case included in this repository.
It shows the evidence chain from processed public-source-derived rows to a
thermal recovery descriptor and a bulk/model-equivalent permeability scale
check.

## Result

The AMU 34 m crop has a post-pump-stop thermal recovery signal that can be fit
with a simple exponential descriptor.

| Quantity | Value |
| --- | ---: |
| Fit window | `2022-04-12 15:32:12` to `2022-04-13 16:00:00` |
| Recovery descriptor | `tau = 4.19 h` |
| Fit residual | `RMSE = 0.0125 °C` |
| Pre-stop median flow | `0.400 L/min` |
| Pressure drop used for boundary calculation | `22.7 MPa` |
| Source-constrained permeability band | `3.52e-16–4.40e-15 m²` |
| Preferred model-equivalent index | `1.59e-15 m²` |

The comparison is a scale check. The preferred `m²` value falls inside nearby
published EGS Collab permeability ranges, but the comparison is not exact same-
sample or exact-fracture validation.

## Reproducible Artifacts

- Recovery fit: [`../artifacts/egs_collab_exp2_amu34m_recovery_fit.png`](../artifacts/egs_collab_exp2_amu34m_recovery_fit.png)
- Permeability scale check: [`../artifacts/egs_collab_exp2_amu34m_k_scale_check.png`](../artifacts/egs_collab_exp2_amu34m_k_scale_check.png)
- Summary JSON: [`../artifacts/egs_collab_exp2_summary.json`](../artifacts/egs_collab_exp2_summary.json)

## Method

The recovery fit uses the AMU 34 m temperature anomaly after pump stop. The
fitted `tau` is a compact recovery-speed descriptor: smaller means faster
relaxation, larger means slower relaxation.

The permeability conversion is not `tau` alone. It uses the boundary calculation

```text
k_eq = mu * Q * L / (A * deltaP)
```

where `Q` is flow, `deltaP` is pressure drop, `mu` is viscosity, and `L/A` is an
explicit geometry assumption. The result is a bulk/model-equivalent permeability
index, not a direct rock measurement.

## Published Comparison

The comparison rows are nearby EGS Collab Experiment 2 permeability ranges from
Meng/Frash-style rock-mechanics context:

- `YA02-05`: `5.92e-16–5.92e-15 m²`
- `YA02-01`: `9.87e-18–7.90e-15 m²`

The useful statement is same-testbed/same-depth-scale numerical consistency.
The source record does not support an exact same-fracture claim.

## Claim Boundary

Allowed:

- one public EGS Collab temperature-recovery crop can be reduced to a recovery descriptor;
- the boundary calculation maps that crop to a bulk/model-equivalent `m²` scale;
- the resulting scale is numerically consistent with nearby published EGS Collab ranges.

Not allowed:

- measured rock permeability;
- exact fracture permeability;
- exact same-sample validation;
- geometry-independent permeability;
- field-scale production forecasting;
- validation of all candidate datasets.

## Sources

- EGS Collab Exp2 public data source: <https://gdr.openei.org/submissions/1428>
- EGS Collab DTS / event-window source: <https://gdr.openei.org/submissions/1476>
- EGS Collab trajectory/context source: <https://gdr.openei.org/submissions/1483>
- Meng et al. 2022 / EGS Collab permeability context: <https://www.osti.gov/biblio/1846146>
- Schwering et al. 2023 / EGS Collab stimulation context: <https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2023/Schwering.pdf>
- Kneafsey et al. 2025 / EGS Collab context: <https://publications.mygeoenergynow.org/grc/1034612.pdf>
- Kneafsey et al. 2024 / EGS Collab context: <https://www.osti.gov/biblio/2481285>
