# Proof Example — EGS Collab Exp2 AMU 34 m

This is one public-data worked example. Its job is to show the evidence chain:

1. find a temperature-recovery signal,
2. fit a simple recovery descriptor,
3. combine that descriptor with source-backed pressure/flow context and explicit geometry assumptions,
4. compare the resulting bulk/model-equivalent permeability scale against nearby published permeability ranges.

This is not a final paper result and not a claim that a specific fracture or core plug was measured by this workflow.

## Short Result

The EGS Collab Exp2 AMU 34 m crop gives a clean thermal-recovery descriptor and a geometry-dependent bulk/model-equivalent permeability scale in `m²`.

- Thermal recovery fit window: `2022-04-12 15:32:12` to `2022-04-13 16:00:00`.
- Fitted recovery descriptor: `tau = 4.19 h`.
- Fit residual scale: `RMSE = 0.0125 °C`.
- Public pressure/flow context used for the boundary calculation: pre-stop median flow `0.400 L/min` and pressure drop `22.7 MPa`.
- Source-constrained permeability band: `3.52e-16–4.40e-15 m²`.
- Preferred model-equivalent index: `1.59e-15 m²`.

The useful claim is narrow: this public-data recovery example lands on the same permeability scale as nearby published EGS Collab rock-mechanics permeability values. It does not prove exact-fracture permeability, geometry-independent permeability, or a field-validated production forecast.

## Static Proof Artifacts

- Thermal recovery panel: [`../artifacts/egs_collab_exp2_amu34m_recovery_fit.png`](../artifacts/egs_collab_exp2_amu34m_recovery_fit.png)
- Permeability scale-check panel: [`../artifacts/egs_collab_exp2_amu34m_k_scale_check.png`](../artifacts/egs_collab_exp2_amu34m_k_scale_check.png)

## What Was Rebuilt

The thermal part asks whether the public data contain a coherent recovery curve after a thermal disturbance. In this crop, the AMU 34 m temperature signal recovers smoothly enough to fit a simple exponential-style descriptor, reported as `tau`. Here, `tau` is a compact measure of recovery speed: smaller means faster recovery, larger means slower recovery.

The permeability part does not treat `tau` alone as permeability. The conversion uses a boundary calculation with pressure, flow, viscosity, a length scale, and an effective area:

```text
k_eq = mu * Q * L / (A * deltaP)
```

For the public packet, this is framed as a bulk/model-equivalent permeability index. It is a way to ask, “what straight-rock permeability scale would be consistent with this pressure-flow boundary and recovery geometry?” It is not a direct measurement of intrinsic fracture permeability.

## Published Comparison

The closest-depth public comparison used here is from Meng/Frash-style EGS Collab rock-mechanics permeability rows near the same depth scale.

- `YA02-05`: `5.92e-16–5.92e-15 m²`.
- `YA02-01`: `9.87e-18–7.90e-15 m²`.

The preferred public-data estimate, `1.59e-15 m²`, sits inside those nearby published ranges. That supports a same-depth-scale consistency claim. It does not make the comparison exact: the published values are not the exact same field crop, not the exact same fracture, and not the same measurement method.

## Claim Boundary

Safe wording:

- “This worked example shows a public EGS Collab temperature-recovery signal that can be reduced to a simple recovery descriptor and mapped to a bulk/model-equivalent permeability scale in `m²`.”
- “The resulting `m²` range is numerically consistent with nearby published EGS Collab permeability ranges at the same depth scale.”
- “This is a credibility example for the workflow, not a final validation of every dataset route.”

Do not claim:

- measured rock permeability,
- exact fracture permeability,
- exact same-sample validation,
- geometry-independent permeability,
- field-scale production forecasting,
- proof that all candidate datasets are usable.

## Caveats

The timing and geometry are good enough for a worked public example, but not perfect. Public geothermal records rarely provide an exact one-to-one match between a temperature crop, a pressure-flow boundary, a known fracture, and a lab permeability value. The honest result is therefore a source-bounded scale check, not an over-precise measurement claim.

The most important remaining assumptions are the effective length `L`, effective area `A`, and the exact comparability tier between the AMU 34 m crop and the published permeability rows. The public packet keeps those assumptions visible because hiding them would make the example look stronger than the evidence allows.

## Sources

- EGS Collab Exp2 public data source: <https://gdr.openei.org/submissions/1428>
- EGS Collab DTS / event-window source: <https://gdr.openei.org/submissions/1476>
- EGS Collab trajectory/context source: <https://gdr.openei.org/submissions/1483>
- Meng et al. 2022 / EGS Collab permeability context: <https://www.osti.gov/biblio/1846146>
- Schwering et al. 2023 / EGS Collab stimulation context: <https://pangea.stanford.edu/ERE/pdf/IGAstandard/SGW/2023/Schwering.pdf>
- Kneafsey et al. 2025 / EGS Collab context: <https://publications.mygeoenergynow.org/grc/1034612.pdf>
- Kneafsey et al. 2024 / EGS Collab context: <https://www.osti.gov/biblio/2481285>
