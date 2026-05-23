# Geothermal recovery screening

Small reproducibility repository for one public-data geothermal thermal-recovery
worked example and related metadata-readiness notes.

The reproducible object is an EGS Collab Experiment 2 AMU 34 m recovery case.
The scripts rebuild a recovery descriptor, a bulk/model-equivalent permeability
scale in `m²`, and two static figures from small processed public-source-derived
inputs.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/reproduce_egs_collab_exp2.py
python scripts/check_reproduction.py
```

Expected regenerated outputs:

- `artifacts/egs_collab_exp2_amu34m_recovery_fit.png`
- `artifacts/egs_collab_exp2_amu34m_k_scale_check.png`
- `artifacts/egs_collab_exp2_summary.json`

Expected checked values:

- `tau_h ≈ 4.19`
- `rmse_c ≈ 0.0125`
- `flow_l_min = 0.400`
- `delta_p_mpa = 22.7`
- `k_eq_preferred_m2 ≈ 1.59e-15`
- `k_eq_band_m2 ≈ 3.52e-16–4.40e-15`

## Claim Boundary

This repository reports a public-data **bulk/model-equivalent permeability scale
check** in `m²` for one EGS Collab worked example. It does not report measured
rock permeability, exact-fracture permeability, geometry-independent
permeability, field validation, or a FORGE permeability estimate.

Utah FORGE August 2025 remains `source-request-needed`: public sources indicate
that relevant forcing streams existed, but the row-level pressure, flow, and
temperature forcing data needed for a responsible permeability calculation have
not been located here.

## Repository Contents

- `data/processed/` — small processed inputs for the EGS Collab worked example.
- `data/provenance/` — source URLs and processing notes for the processed inputs.
- `params/` — case parameters and expected values.
- `scripts/reproduce_egs_collab_exp2.py` — rebuilds figures and summary JSON.
- `scripts/check_reproduction.py` — verifies expected numeric values and outputs.
- `artifacts/` — regenerated static figures and summary JSON.
- `docs/egs_collab_exp2_worked_example.md` — method and interpretation for the worked example.
- `docs/forge_aug2025_metadata_request.md` — why FORGE is metadata-blocked.
- `docs/evidence_labels.md` — status labels used for source-backed claims.
- `docs/sources.md` — public sources used by this repository.

## Data Policy

This repository intentionally excludes raw HDF5 files, ZIP exports, NetCDF
files, private notes, candidate-funnel files, and unpublished source rows. The
included CSVs are small processed snippets for reproducing the worked example;
they are not substitutes for the upstream public datasets or papers.

## Citation And Reuse

This is preliminary research code and supporting material. Code reuse is covered
by `LICENSE` once present. Text, figures, processed snippets, and upstream-source
reuse caveats are described in `NOTICE.md` once present.
