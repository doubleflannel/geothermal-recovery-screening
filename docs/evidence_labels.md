# Evidence labels

This repository separates what the public rows support, what is assumed, and
what is still missing. The labels keep a useful thermal-recovery screen from
turning into an overstated permeability claim.

## Plain-language status labels

| Label | Plain meaning | Allowed public use |
| --- | --- | --- |
| `Validated / qualified` | A thermal-recovery-derived `m²` estimate has an independent published permeability-scale comparison. The comparison may still be same-depth-scale or same-field rather than exact same sample. | Say the estimate is validated or qualified at the stated comparison tier. Keep the caveat visible. |
| `Discovery-only` | The public rows and metadata support a defensible thermal-recovery estimate, but there is no independent numeric permeability comparator yet. | Report the `m²` estimate as exploratory or discovery-only. Do not call it validation. |
| `Source-request-needed` | A paper, report, or portal indicates the missing stream probably exists, but the needed row-level data or metadata are not public here. | Write a narrow request for exact fields, timestamps, units, depth references, and channel definitions. Do not quote a permeability result. |
| `Metadata limitation` | The route is scientifically useful as a warning example, but timing, channel definitions, depth mapping, or alignment metadata are too weak for a permeability calculation. | Use as a claim-boundary or blocker example. Do not count it as a result. |
| `Support-only` | The route gives hydraulic or context evidence, but it is not a raw thermal-recovery-to-`m²` case. | Use as an appendix or scale check, not as Purwamaska and Fulton 2026-style thermal-recovery validation. |
| `Hydraulic support` | Pressure-flow, falloff, transmissivity, or productivity-index evidence can reproduce or contextualize permeability scale, but it does not start from temperature recovery. | Use as supporting comparator material only unless a temperature-recovery bridge is added. |

## Fit-readiness labels

These labels describe why a route can or cannot be computed yet.

| Label | Meaning | Allowed use |
| --- | --- | --- |
| `fit-ready` | Temperature recovery rows, pressure/flow/temperature forcing, timing, units, and geometry metadata are sufficient for a bounded calculation. | Compute a bulk/model-equivalent permeability scale in `m²` with stated assumptions. |
| `partial-adjacent-found` | Related streams exist in public sibling sources, but the package is incomplete or not yet aligned. | Use for context, window selection, or a follow-up alignment task. |
| `source-request-needed` | A report or paper indicates the missing stream likely exists, but the row-level file or metadata was not located publicly. | Write a narrow request for the missing fields, timestamps, units, and channel definitions. |
| `model-bridge-blocked` | Rows exist, but the thermal-to-permeability physics bridge is not defensible yet. | Keep the data route alive while treating the model conversion as the blocker. |
| `supporting-comparator` | A pressure-flow, falloff, transmissivity, or productivity-index calculation checks a permeability scale but is not a thermal-recovery case. | Use as an appendix or context check, not as Purwamaska and Fulton 2026-style validation. |

## Source status

| Status | Definition | Example |
| --- | --- | --- |
| `source-confirmed` | A public source directly states the unit, timestamp convention, channel meaning, depth reference, or operation window. | A dataset page says temperature is in degrees Celsius and depth is measured depth in meters. |
| `assumption-labeled` | The calculation proceeds only after a declared interpretation or sensitivity bound. | A geometry area is varied because the exact active contact area is not published. |
| `unknown` | The repo has not located enough evidence to support the value or mapping. | A plotted flow curve exists, but the row-level file and channel definition are not public. |

## Minimum metadata for a thermal-recovery permeability screen

A thermal-recovery permeability screen needs:

- temperature recovery rows with timestamps, units, depth, and sensor identity;
- overlapping pressure rows with units, sensor location, and well name;
- overlapping flow-rate rows with units and sign convention;
- inlet, injection, production, or wellhead temperature rows that define the thermal forcing;
- timestamp convention for every stream;
- operation-state context for injection, shut-in, circulation, and flowback intervals;
- depth reference and geometry basis for length and area sensitivity;
- fluid assumptions or source-backed bounds for density and viscosity;
- channel definitions for pressure, flow, and temperature columns;
- an independent comparison source if the result is called validation.

Without the forcing rows, a temperature curve can still be screened, but it
cannot by itself define permeability.

## Claim boundary

The current public release features Brady/PoroTomo as the verified/qualified threshold-compatible example and retains EGS Collab as a below-threshold control. The
project identity is the screening ladder across public thermal-recovery routes.
A route can be counted only when the evidence supports the stated label. A
worked example is not measured fracture permeability, exact same-sample
validation, or evidence that every candidate dataset is usable.

Pressure-flow-only, falloff-only, transmissivity-only, and productivity-index
routes are not Purwamaska and Fulton 2026-style thermal-recovery validation. They can be
useful supporting evidence, but they do not count unless a raw temperature
recovery and thermal-to-`m²` bridge are added.
