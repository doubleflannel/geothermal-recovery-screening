# Release readiness checklist

This checklist is for a future versioned public release or possible Zenodo DOI
for `geothermal-recovery-screening`. This task does **not** create a release,
tag, archive, or DOI.

## Candidate release identity

- Tag name: `v0.1.0` for the first stable public worked-example release.
- Release title: `EGS Collab Exp2 thermal-recovery worked example`.
- DOI decision: defer Zenodo DOI until the README, notebook, dataset catalog,
  citation/reuse language, and public QC have passed a final review.

## Include

- `README.md`
- `CITATION.cff`
- `LICENSE`
- `NOTICE.md`
- `requirements.txt`
- `params/egs_collab_exp2.yml`
- `scripts/reproduce_egs_collab_exp2.py`
- `scripts/check_reproduction.py`
- `data/processed/*.csv`
- `data/provenance/egs_collab_exp2_sources.yml`
- `docs/*.md`
- `notebooks/egs_collab_exp2_worked_example.ipynb`
- `artifacts/egs_collab_exp2_amu34m_recovery_fit.png`
- `artifacts/egs_collab_exp2_amu34m_k_scale_check.png`
- `artifacts/egs_collab_exp2_summary.json`

## Exclude

- raw HDF5, ZIP, NetCDF, LAS, XLSX, or full upstream dataset exports;
- private notes, Backlog task files, `.codex`, `.tmp`, local screenshots, and
  local browser artifacts;
- candidate-funnel internals not intended for public review;
- any source rows that are not already cleared as small processed
  reproducibility snippets;
- any claim that unresolved routes are permeability results.

## Reproduction gate

Before tagging a release, run:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/reproduce_egs_collab_exp2.py
python scripts/check_reproduction.py
```

The release is not ready unless the checker confirms:

- `tau_h ≈ 4.19`
- `rmse_c ≈ 0.0125`
- `flow_l_min = 0.400`
- `delta_p_mpa = 22.7`
- `k_eq_preferred_m2 ≈ 1.59e-15`
- `k_eq_band_m2 ≈ 3.52e-16–4.40e-15`

## Claim-boundary gate

Before tagging, confirm the public text does not claim:

- measured rock permeability;
- exact-fracture permeability;
- exact same-sample validation;
- geometry-independent permeability;
- field-scale forecasting;
- a permeability result for unresolved candidate datasets;
- pressure-flow-only routes as Purwamaska and Fulton 2026-style thermal-recovery
  validation.

Allowed wording should stay close to:

> This repository provides one public-data bulk/model-equivalent permeability
> scale check for an EGS Collab Exp2 thermal-recovery worked example.

## DOI gate

Only create a Zenodo DOI after:

- the release checklist passes;
- the user approves permanent archiving;
- the citation metadata are final enough for public use;
- the README and `NOTICE.md` clearly separate this repository from upstream raw
  data and publications.

Do not create a DOI from this checklist alone.
