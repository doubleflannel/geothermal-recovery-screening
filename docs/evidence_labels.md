# Evidence labels

This repository separates source-backed facts, declared assumptions, and missing
metadata. The labels are used to keep a useful screen from turning into an
overstated permeability claim.

## Status Labels

| Label | Meaning | Allowed use |
| --- | --- | --- |
| `fit-ready` | Temperature recovery rows, pressure/flow/temperature forcing, timing, units, and geometry metadata are sufficient for a bounded calculation. | Compute a bulk/model-equivalent permeability scale in `m²` with stated assumptions. |
| `partial-adjacent-found` | Related streams exist in public sibling sources, but the package is incomplete or not yet aligned. | Use for context, window selection, or a follow-up alignment task. |
| `source-request-needed` | A report or paper indicates the missing stream likely exists, but the row-level file or metadata was not located publicly. | Write a narrow request for the missing fields, timestamps, units, and channel definitions. |
| `model-bridge-blocked` | Rows exist, but the thermal-to-permeability physics bridge is not defensible yet. | Keep the data route alive while treating the model conversion as the blocker. |
| `supporting-comparator` | A pressure-flow, falloff, transmissivity, or productivity-index calculation checks a permeability scale but is not a thermal-recovery case. | Use as an appendix or context check, not as Purwamaska/Fulton-style validation. |

## Source Status

| Status | Definition | Example |
| --- | --- | --- |
| `source-confirmed` | A public source directly states the unit, timestamp convention, channel meaning, depth reference, or operation window. | A dataset page says temperature is in degrees Fahrenheit and depth is in feet. |
| `assumption-labeled` | The calculation proceeds only after a declared interpretation or sensitivity bound. | A timezone is assigned to a timestamp column that lacks an explicit timezone statement. |
| `unknown` | The repo has not located enough evidence to support the value or mapping. | A flow column exists in a paper figure but the row-level file and channel definition are not public. |

## Minimum Fit-Ready Metadata

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

## Claim Boundary

The current EGS Collab case is a worked example: one public recovery signal is
reduced to a recovery descriptor and compared as a bulk/model-equivalent `m²`
scale check. It is not measured fracture permeability, exact same-sample
validation, or evidence that every candidate dataset is usable.
