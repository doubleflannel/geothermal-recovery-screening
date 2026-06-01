# Data

This directory contains small processed public-source-derived inputs for the
Brady/PoroTomo worked example inside the public geothermal thermal-recovery
screening framework. It intentionally does not contain raw HDF5 files, raw ZIP
exports, full private processed datasets, candidate-funnel files, or unpublished
source rows.

## Files

- `processed/brady_porotomo_56_1_recovery_descriptors.csv` - processed Brady/PoroTomo 56-1 recovery descriptors used by the public slug-drainage reproduction script.
- `processed/brady_porotomo_56_1_recovery_fit_curve.csv` - small processed hourly temperature recovery and fitted-curve snippet used for the public figure.
- `processed/brady_porotomo_56_1_alignment_summary.json` - small public-safe alignment summary for the Brady/PoroTomo DTS, pressure, and pumping window.
- `provenance/brady_porotomo_56_1_sources.yml` - source URLs, local derivation notes, and claim boundaries for the Brady/PoroTomo public snippets.

These files are for reproducibility of the lightweight worked example. They are
not a replacement for the original public datasets or papers, and they do not
represent the full active screening set.
