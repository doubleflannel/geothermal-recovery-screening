# Data

This directory contains small processed public-source-derived inputs for the EGS Collab Exp2 AMU 34 m worked example. It intentionally does not contain raw HDF5 files, raw ZIP exports, full private processed datasets, candidate-funnel files, or unpublished source rows.

## Files

- `processed/egs_collab_exp2_amu34m_recovery.csv` — post-pump-stop temperature-recovery crop at AMU 34 m with the fitted recovery curve used by the worked example.
- `processed/egs_collab_exp2_boundary_inputs.csv` — pressure, flow, viscosity, geometry, and fitted-descriptor values used to rebuild the bulk/model-equivalent permeability index.
- `processed/egs_collab_exp2_published_k_ranges.csv` — nearby published EGS Collab permeability ranges used only as a scale check.
- `provenance/egs_collab_exp2_sources.yml` — source URLs, local derivation notes, and claim boundaries.

These files are for reproducibility of the lightweight worked example. They are not a replacement for the original public datasets or papers.
