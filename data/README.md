# Data

This directory contains small processed public-source-derived inputs for the
reproducible worked examples inside the public geothermal thermal-recovery
screening framework. It intentionally does not contain raw HDF5 files, raw ZIP
exports, full private processed datasets, candidate-funnel files, or unpublished
source rows.

## Files

- `processed/egs_collab_exp2_amu34m_recovery.csv` — post-pump-stop temperature-recovery crop at AMU 34 m with the fitted recovery curve used by the worked example.
- `processed/egs_collab_exp2_boundary_inputs.csv` — pressure, flow, viscosity, geometry, and fitted-descriptor values used to rebuild the bulk/model-equivalent permeability index.
- `processed/egs_collab_exp2_published_k_ranges.csv` — nearby published EGS Collab permeability ranges used only as a scale check.
- `provenance/egs_collab_exp2_sources.yml` — source URLs, local derivation notes, and claim boundaries.
- `processed/brady_porotomo_56_1_recovery_descriptors.csv` — processed Brady/PoroTomo 56-1 recovery descriptors used by the public slug-drainage reproduction script.
- `processed/brady_porotomo_56_1_alignment_summary.json` — small public-safe alignment summary for the Brady/PoroTomo DTS, pressure, and pumping window.
- `provenance/brady_porotomo_56_1_sources.yml` — source URLs, local derivation notes, and claim boundaries for the Brady/PoroTomo public snippets.

These files are for reproducibility of the lightweight worked examples. They
are not a replacement for the original public datasets or papers, and they do
not represent the full active screening set.
