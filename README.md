# Geothermal recovery screening

This repository is a small public-data test of a Purwamaska/Fulton-style idea:
a borehole temperature-recovery curve after circulation can be compared with a
physics-based boundary model to estimate a bulk/model-equivalent permeability
scale in `m²`.

The starting point is the method, not this repository. Purwamaska and Fulton
show that thermal recovery can carry permeability information when the timing,
pressure/flow forcing, thermal forcing, geometry, and observation location are
made explicit. This repo asks a narrower reproducibility question: can that same
style of reasoning be demonstrated from small public-source-derived rows?

The worked example is one EGS Collab Experiment 2 AMU 34 m recovery case. It
rebuilds a thermal-recovery descriptor, a pressure/flow/geometry-based
permeability scale, and static comparison figures from included processed
inputs.

## What this repo proves

This repo shows that one public-data recovery window can be traced through the
same basic evidence ladder a Purwamaska/Fulton-style review needs:

1. processed temperature, pressure, and flow rows from public-source-derived
   inputs;
2. a fitted recovery descriptor, `tau`, for the AMU 34 m temperature curve;
3. a declared boundary calculation, `k_eq = mu * Q * L / (A * deltaP)`;
4. a bulk/model-equivalent permeability band in `m²`;
5. a nearby published EGS Collab permeability-scale comparison.

The result is a scale check, not a direct rock measurement. The preferred value
is `1.59e-15 m²`, with a source-constrained band of
`3.52e-16–4.40e-15 m²`.

## Reproduce

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/reproduce_egs_collab_exp2.py
python scripts/check_reproduction.py
```

Expected regenerated outputs:

- `artifacts/egs_collab_exp2_amu34m_recovery_fit.png` — measured recovery curve
  and exponential descriptor fit.
- `artifacts/egs_collab_exp2_amu34m_k_scale_check.png` — model-equivalent
  `m²` band compared with nearby published EGS Collab ranges.
- `artifacts/egs_collab_exp2_summary.json` — machine-readable fitted values,
  forcing values, and claim boundary.

Expected checked values:

- `tau_h ≈ 4.19`
- `rmse_c ≈ 0.0125`
- `flow_l_min = 0.400`
- `delta_p_mpa = 22.7`
- `k_eq_preferred_m2 ≈ 1.59e-15`
- `k_eq_band_m2 ≈ 3.52e-16–4.40e-15`

## Readable demo

- `notebooks/egs_collab_exp2_worked_example.ipynb` walks through the same case
  as a reviewer-facing notebook.
- The scripts remain the canonical reproduction path; the notebook is a readable
  companion for inspecting the calculation.

## Evidence boundary

Allowed statement:

> The EGS Collab Exp2 AMU 34 m worked example gives a public-data
> bulk/model-equivalent permeability scale check that is numerically consistent
> with nearby published EGS Collab permeability ranges.

Not claimed:

- measured rock permeability;
- exact-fracture permeability;
- exact same-sample validation;
- geometry-independent permeability;
- field-scale forecasting;
- a permeability result for unresolved candidate datasets.

Candidate and blocked routes are listed in `docs/dataset_catalog.md`; the status
terms are defined in plain language in `docs/evidence_labels.md`. A blocked or
source-request route is not counted as a permeability result here. The method
basis comes from Purwamaska/Fulton-style thermal recovery; the counted result
here is this repository's public-data worked example, not a universal method
validation.

## Repository contents

- `data/processed/` — small processed inputs for the EGS Collab worked example.
- `data/provenance/` — source URLs and processing notes for the processed inputs.
- `params/` — case parameters and expected values.
- `scripts/reproduce_egs_collab_exp2.py` — rebuilds figures and summary JSON.
- `scripts/check_reproduction.py` — verifies expected numeric values and outputs.
- `notebooks/egs_collab_exp2_worked_example.ipynb` — readable walkthrough of the
  worked example.
- `artifacts/` — regenerated static figures and summary JSON.
- `docs/egs_collab_exp2_worked_example.md` — method and interpretation for the
  worked example.
- `docs/dataset_catalog.md` — compact status catalog for screened routes.
- `docs/evidence_labels.md` — status labels used for source-backed claims.
- `docs/release_readiness_checklist.md` — checklist for a future versioned release or DOI decision.
- `docs/sources.md` — public sources used by this repository.

## Data policy

This repository intentionally excludes raw HDF5 files, ZIP exports, NetCDF
files, private notes, candidate-funnel files, and unpublished source rows. The
included CSVs are small processed snippets for reproducing the worked example;
they are not substitutes for the upstream public datasets or papers.

## Citation and reuse

If this repository is useful, cite it as preliminary research software using
`CITATION.cff`. Code reuse is covered by `LICENSE`.

Text, figures, processed snippets, and upstream-source reuse caveats are
explained in `NOTICE.md`. The included CSVs are small reproducibility snippets,
not a new raw-data archive and not a blanket reuse license for the original EGS
Collab datasets, papers, or reports. Check the upstream sources in
`docs/sources.md` and `data/provenance/egs_collab_exp2_sources.yml` before
reusing source-derived materials.
