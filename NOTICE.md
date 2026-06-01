# Notice

This repository is a preliminary research-code release. It contains code,
small processed public-source-derived inputs, static figures, and documentation
for a public-data geothermal thermal-recovery screening framework. The current
release includes one featured Brady/PoroTomo verified example, one reproducible EGS Collab below-threshold control, plus a public
dataset-route catalog.

## Code

Repository code is licensed under the MIT License in `LICENSE`.

## Text, Figures, And Processed Inputs

The text, figures, processed CSV snippets, and summary JSON are included to make
the screening framework and worked example inspectable. They are not a blanket
grant of rights to the underlying public datasets, papers, reports, or
third-party source materials.

If you reuse these materials, cite this repository and check the upstream source
terms for the original data and publications.

## Upstream Sources

The processed inputs derive from public-source context listed in:

- `data/provenance/egs_collab_exp2_sources.yml`
- `docs/sources.md`

This repository does not redistribute raw HDF5, ZIP, NetCDF, LAS, or full
public-dataset exports.

## Scientific Boundary

The repository reports claim-bounded bulk/model-equivalent permeability
screening results in `m²` only when the evidence ladder supports them. The
included Brady/PoroTomo example is one qualified same-field/fault-scale check; it is not measured rock
permeability, exact-fracture permeability, field validation, or a FORGE
permeability estimate.
