# FORGE August 2025 Request Rationale

This page explains why the Utah FORGE August 2025 16B(78)-32 huff-and-puff / circulation dataset is worth a targeted metadata request, and why it is not yet a permeability result.

## Decision

`source-request-needed`

The public DTS package is promising, but the public packet I could inspect does not include the row-level pressure, flow, and temperature forcing needed to compute a defensible thermal-recovery permeability estimate in `m²`.

## Why This Candidate Is Promising

The DTS side is unusually strong for a public geothermal screen.

- [GDR 1826](https://gdr.openei.org/submissions/1826) provides processed Neubrex DTS data from well `16B(78)-32` during August 2025 circulation and huff-and-puff operations. The GDR page states that the files include calibrated DTS temperature data in HDF5 form, depth values, timestamp arrays, temperature in degrees Fahrenheit, and depth in feet.
- [GDR 1822](https://gdr.openei.org/submissions/1822) provides the linked fiber-optic monitoring report. The GDR page describes cross-well circulation and huff-and-puff testing in August 2025, with continuous RFS-DSS, DTS, and DAS monitoring along the cased section of production well `16B`.
- [Ifrene et al. 2026](https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Ifrene.pdf) describes the same August 2025 huff-puff diagnostic campaign. The paper reports multiple cyclic injection/flowback steps, including `2.5`, `5.0`, and `7.5 bpm` rate steps, and says surface flow, temperature, and pressure were logged continuously while fiber-optic data were collected.

That is the right kind of experiment for a public thermal-recovery screen: distributed temperature response plus known injection/flowback operations. The current blocker is not that the experiment is weak. The blocker is that the public files found so far do not expose the forcing rows that define the heat and flow input.

## What Is Missing

The missing item is a row-level Liberty/Pason forcing export for the main huff-and-puff window:

- date window: `2025-08-26` through `2025-08-30`;
- timestamp convention and timezone;
- sampling cadence;
- pressure, flow, and temperature rows that overlap the DTS HDF5 interval;
- channel definitions and sensor locations;
- whether the values are raw, filtered, corrected, or merged from Liberty/Pason sources.

The specific fields requested are:

- `timestamp` with timezone/time basis;
- `16A Wellhead PSI (PSI)`;
- `16B WH Press. North (PSI)`;
- `16B 3" Flow - 2 (BPM)`;
- `Separator Flow North (BPM)`;
- `Separator Flow South (BPM)`;
- `16B 2" Flow (BPM)`;
- `Injection Temp (deg F)`;
- `16B 3" Flow (BPM)`;
- `16B WH Temp (deg F)`;
- `16B Coil Tubing PSI (1K Sensor)`;
- `Choke Pressure (PSI)`;
- `Liberty Discharge Press. (PSI)`;
- `Liberty Pumpstroke Flow R (BPM)`;
- `Liberty Turbine Flow Rate (BPM)`;
- `Liberty Total Volume (BBL)`.

If the full export cannot be shared, a header-only file plus a small Aug. 26–30 sample would still answer the key metadata question: is this candidate fit-ready or only source-request blocked?

## Why GDR 1764 Does Not Unblock It

[GDR 1764](https://gdr.openei.org/submissions/1764) is useful background because it provides shut-in wellhead pressure data for wells `16A(78)-32` and `16B(78)-32`. The GDR page states that pressure is reported in `PSI` with timestamps in date/time format, covering a September 2024–April 2025 period and a June–August 2025 period.

It does not solve this specific candidate. The inspected public GDR 1764 package is pressure-only, does not provide flow or injection/production temperature, and does not provide the row-level Aug. 26–30 huff-and-puff forcing package needed to pair with the DTS recovery window.

## Minimum Metadata Needed To Move Forward

To turn this from `source-request-needed` into `fit-ready`, the public record needs:

- row-level pressure, flow, and temperature values for Aug. 26–30, 2025;
- timestamps with timezone and clock convention;
- units for every channel;
- well and measurement location for every pressure/flow/temperature channel;
- operation-state labels or enough rows to reconstruct injection, shut-in, and flowback intervals;
- documentation of whether each stream is raw, corrected, filtered, or merged;
- confirmation that the forcing rows overlap the DTS HDF5 timestamps;
- enough geometry/depth metadata to connect thermal response depth to the active interval being forced.

## Claim Boundary

Safe wording:

- “The Utah FORGE August 2025 16B DTS package is a promising public candidate for a thermal-recovery permeability screen.”
- “The candidate is currently `source-request-needed` because the row-level Liberty/Pason pressure-flow-temperature forcing export was not found in the public package inspected.”
- “The request is narrow: identify or provide the forcing rows and metadata for Aug. 26–30, 2025.”

Do not claim:

- FORGE August 2025 permeability has been estimated;
- FORGE August 2025 permeability has been validated;
- DTS alone is enough to compute permeability;
- GDR 1764 supplies the missing Aug. 26–30 forcing;
- the Liberty/Pason rows are public until a public file or authorized source confirms them.
