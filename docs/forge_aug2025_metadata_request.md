# FORGE August 2025 metadata request

Status: `source-request-needed`

The Utah FORGE August 2025 16B(78)-32 DTS record is a promising candidate for a
thermal-recovery screen, but this repository does not include a FORGE
permeability estimate. The blocker is missing row-level forcing data and channel
metadata for the same August 2025 huff-and-puff / circulation interval.

## Public Evidence

- [GDR 1826](https://gdr.openei.org/submissions/1826) describes processed
  Neubrex DTS data from well `16B(78)-32`, including HDF5 temperature data,
  depth values, timestamp arrays, temperature in degrees Fahrenheit, and depth in
  feet.
- [GDR 1822](https://gdr.openei.org/submissions/1822) describes the associated
  fiber-optic monitoring report for August 2025 cross-well circulation and
  huff-and-puff testing.
- [Ifrene et al. 2026](https://pangea.stanford.edu/ERE/db/GeoConf/papers/SGW/2026/Ifrene.pdf)
  describes cyclic injection and flowback steps during the same diagnostic
  campaign and states that surface flow, temperature, and pressure were logged
  while fiber-optic data were collected.
- [GDR 1764](https://gdr.openei.org/submissions/1764) provides useful shut-in
  pressure context, but it does not provide the pressure-flow-temperature forcing
  package for the August 26–30, 2025 DTS interval.

## Missing Metadata

The required missing package is row-level pressure, flow, and temperature
forcing for the August 26–30, 2025 interval, with:

- timestamps and timezone/clock convention;
- sampling cadence;
- units for each stream;
- channel definitions and sensor locations;
- well names and operation state;
- raw/processed status;
- enough overlap with the DTS timestamps to test alignment.

If the full export cannot be shared, a header plus a short representative sample
would still decide whether the candidate moves from `source-request-needed` to a
fit-ready alignment task.

## Claim Boundary

Allowed:

- the public DTS record and reports make FORGE August 2025 worth a targeted
  metadata request;
- the current blocker is missing row-level forcing data and channel metadata;
- GDR 1764 is useful pressure context but does not unblock the huff-and-puff
  thermal-recovery calculation.

Not allowed:

- FORGE August 2025 permeability has been estimated;
- DTS alone is sufficient for permeability;
- pressure, flow, and DTS are source-confirmed aligned;
- GDR 1764 supplies the missing August 26–30 forcing package;
- a Liberty/Pason row-level export is public unless a public source or
  authorized data provider confirms it.
