# Release readiness checklist

This checklist is for a future versioned public release or possible Zenodo DOI
for `geothermal-recovery-screening`. This task does **not** create a release,
tag, archive, or DOI.

## Candidate release identity

- Tag name: `v0.1.0` for the first stable public screening-framework release.
- Release title: `Public geothermal thermal-recovery screening framework`.
- DOI decision: defer Zenodo DOI until the README, dataset catalog,
  citation/reuse language, and public QC have passed a final review.

## Include

- `README.md`
- `CITATION.cff`
- `LICENSE`
- `NOTICE.md`
- `requirements.txt`
- `scripts/reproduce_brady_porotomo_56_1.py`
- `scripts/check_reproduction.py`
- `data/processed/brady_porotomo_56_1_recovery_descriptors.csv`
- `data/processed/brady_porotomo_56_1_alignment_summary.json`
- `data/provenance/brady_porotomo_56_1_sources.yml`
- `docs/*.md`
- `artifacts/brady_porotomo_56_1_dts_alignment.png`
- `artifacts/brady_porotomo_56_1_slug_bridge.png`
- `artifacts/brady_porotomo_56_1_summary.json`

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
python scripts/reproduce_brady_porotomo_56_1.py
python scripts/check_reproduction.py
```

The release is not ready unless the checker confirms:

- `tau_h ≈ 118.08`
- `rmse_c ≈ 0.472`
- `k_eq_central_m2 ≈ 7.35e-14`
- `k_eq_preferred_range_m2 ≈ 6.26e-15–9.11e-13`

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

> This repository demonstrates a public-data evidence ladder for deciding when
> geothermal temperature-recovery records can support claim-bounded
> bulk/model-equivalent permeability estimates.

It is also acceptable to say that the current release includes one featured
Brady/PoroTomo verified example as an inspectable implementation of the ladder.

## DOI gate

Only create a Zenodo DOI after:

- the release checklist passes;
- the user approves permanent archiving;
- the citation metadata are final enough for public use;
- the README and `NOTICE.md` clearly separate this repository from upstream raw
  data and publications.

Do not create a DOI from this checklist alone.
