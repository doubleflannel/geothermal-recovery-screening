# Evidence Discipline

This packet uses public data to test whether thermal-recovery signals can support bulk/model-equivalent permeability estimates in `m²`. The rule is simple: a result can be interesting before it is final, but the label must say exactly what is confirmed, what is assumed, and what is still missing.

## Evidence Labels

### `fit-ready`

A case is `fit-ready` when the public record has enough information to fit a thermal-recovery descriptor and connect it to a source-backed pressure/flow/temperature boundary.

Plain meaning: the temperature signal, forcing history, timing, units, and geometry are all good enough to make a bounded permeability calculation in `m²`.

### `partial-adjacent-found`

A case is `partial-adjacent-found` when related public sources exist, but they do not yet form a complete calculation package.

Plain meaning: there are useful pieces nearby, such as DTS in one submission and pressure in another, but the pieces still need timing, channel, or depth alignment before they can support a permeability estimate.

### `source-request-needed`

A case is `source-request-needed` when the public record strongly suggests the missing stream exists, but the row-level file or metadata is not public in the inspected package.

Plain meaning: the report or paper shows the data were collected, but the rows needed for calculation are not available yet. The next step is a narrow request for the exact fields, timestamps, units, and metadata.

### `model-bridge-blocked`

A case is `model-bridge-blocked` when the public rows exist, but the physics needed to convert the observed signal into permeability is not yet defensible.

Plain meaning: the measurements are visible, but the conversion is the weak link. This often happens when heat transfer involves multiphase fluids, uncertain geometry, unknown boundary conditions, or a thermal-front process that cannot be represented by the simple model.

## Source-Confirmed Versus Assumption-Labeled

`Source-confirmed` means a public source states the fact directly: timestamp convention, units, channel meaning, measurement location, depth reference, or operation window.

`Assumption-labeled` means the calculation can proceed only if an interpretation is declared up front. Assumptions are allowed for exploratory screens, but they cannot be hidden or described as source-confirmed.

Examples:

- If a data page says temperature is in degrees Fahrenheit and depth is in feet, those units are source-confirmed.
- If a CSV has a `Time` column but no timezone, a timezone choice is assumption-labeled.
- If a report plots flow rate but does not release the row-level flow file, the flow history is not fit-ready.
- If a figure compares to published permeability from a nearby interval, that is a comparability tier, not exact same-sample validation.

## Minimum Metadata For A P/F Thermal-Recovery Permeability Estimate

For this packet, `P/F` means a Purwamaska/Fulton-style thermal-recovery screen: use a temperature recovery signal after circulation, shut-in, huff-and-puff, or a comparable thermal disturbance, then convert the recovery response to a bulk/model-equivalent permeability scale in `m²`.

A case needs the following minimum metadata before it can be treated as `fit-ready`:

- raw or processed temperature recovery rows with timestamps, units, depth, and sensor identity;
- pressure rows that overlap the thermal event, with units, sensor location, and well name;
- flow-rate rows that overlap the same event, with units, sign convention, and injection/production/flowback meaning;
- inlet, injection, production, or wellhead temperature rows that define the thermal forcing;
- timestamp convention for every stream, including timezone and any fixed-offset or daylight-saving behavior;
- operation-state context: injection, shut-in, flowback, circulation, rate steps, and stop/start times;
- depth reference and geometry: measured depth versus true vertical depth, well/fiber depth mapping, active interval, length scale, and effective area or the basis for sensitivity bounds;
- fluid assumptions: water, brine, CO2, steam, or multiphase state; density and viscosity source or defensible bounds;
- channel definitions: what each pressure, flow, and temperature column physically measures and where it is installed;
- public comparison context if the result is called validation rather than an exploratory discovery estimate.

Without the forcing rows, a temperature curve can still be useful, but it cannot by itself define permeability. The temperature curve shows that heat changed. The pressure-flow-temperature boundary explains what caused the change and lets the calculation ask what permeability scale is consistent with it.

## Why Missing Forcing Rows Block Permeability

Thermal recovery is not just “fit a cooling curve and call it permeability.” The same cooling shape can come from different combinations of flow rate, pressure drop, inlet temperature, geometry, fluid properties, and heat-transfer delay.

That is why missing pressure, flow, or inlet-temperature rows are a real blocker. If those rows are missing, the result may still be a useful screen, but it should be labeled `source-request-needed` or `partial-adjacent-found`, not `fit-ready`.

## What This Packet Can And Cannot Claim

This packet can claim:

- public datasets can be screened with a visible evidence ladder;
- one worked EGS Collab example has a source-bounded thermal-recovery descriptor and a bulk/model-equivalent `m²` scale check;
- Utah FORGE August 2025 is a promising but source-request-needed candidate;
- missing metadata are being treated as scientific limits, not ignored.

This packet cannot claim:

- every candidate dataset is usable;
- DTS alone proves permeability;
- pressure-flow-only checks are Purwamaska/Fulton thermal-recovery validation;
- a model-equivalent `m²` value is the same as measured fracture permeability;
- a nearby published permeability range is exact same-sample validation unless the source proves that match.
