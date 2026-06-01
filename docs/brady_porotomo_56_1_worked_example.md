# Brady/PoroTomo 56-1 cold-slug DTS verified example

This is the current featured verified/qualified public-data example for the repository.
It replaces EGS Collab as the headline proof case because the EGS Collab AMU
example is source-constrained below the approximate `1e-14 m²` range where the
Purwamaska and Fulton 2026-style thermal-recovery method becomes effective in
the motivating model setting.

## Result

- Status: `Validated / qualified`.
- Central model-equivalent permeability: `7.35e-14 m²`.
- Preferred geometry/head envelope: `6.26e-15–9.11e-13 m²`.
- Full sensitivity envelope: `3.61e-16–2.73e-11 m²`.
- Independent comparison context: Patterson pressure-model values are mostly
  `2.24e-14–6.62e-14 m²`.

## Why it counts

The public/source-derived DTS recovery rows show a cold-slug thermal recovery
signal. The route extracts a thermal descriptor, maps the slug-drainage response
to a bulk/model-equivalent `k_eq`, and compares that scale against independent
same-field/fault-scale permeability context. The comparison is not exact
same-sensor or exact outflow-patch validation, but it is strong enough for a
qualified threshold-compatible example.

## Claim boundary

Allowed:

- Brady/PoroTomo 56-1 is a qualified validation-style public-data route.
- The comparison tier is same-field/fault-scale same-order support.
- The number is a bulk/model-equivalent slug-drainage estimate, not measured rock
  permeability.

Not claimed:

- exact fracture permeability;
- exact outflow-patch validation;
- measured core permeability;
- source-confirmed outflow geometry;
- full Purwamaska and Fulton simulation validation.

## Featured artifacts

- `artifacts/brady_porotomo_56_1_dts_alignment.png`
- `artifacts/brady_porotomo_56_1_slug_bridge.png`
- `artifacts/brady_porotomo_56_1_summary.json`

## EGS Collab status

The EGS Collab AMU example remains scientifically useful as a reproducible
below-threshold control, but it should not be used as the headline evidence that
the public-data screen finds a threshold-compatible route. Its source-constrained
preferred value is `1.59e-15 m²`, with band `3.52e-16–4.40e-15 m²`.
