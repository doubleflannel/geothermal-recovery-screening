# Open Geothermal Thermal-Recovery Screening

This is a preliminary public-data research packet for testing whether geothermal
temperature-recovery records can support careful, source-backed permeability
screening.

The near-term goal is modest: show that the workflow is serious enough to review
and to justify narrow metadata/data requests. This is not a final paper, not a
peer-reviewed study, and not a claim that every candidate dataset is ready for
permeability interpretation.

## What This Packet Is

This packet documents a small part of an ongoing effort to screen public
geothermal datasets using thermal recovery after circulation, shut-in, or
similar thermal disturbances.

The focus is on reproducibility and claim discipline:

- use public source material where possible;
- separate source-confirmed metadata from assumptions;
- keep time basis, units, depth reference, pressure, flow, and temperature
  forcing explicit;
- report permeability only as bulk/model-equivalent permeability in `m²` when
  the source evidence supports it;
- label blockers instead of smoothing over missing metadata.

## Current Status

One worked public-data proof example is included from an EGS Collab Exp2 case.
That example shows the style of analysis and claim boundary. It does not claim
that the method is fully validated across many datasets.

Utah FORGE August 2025 16B(78)-32 is currently a promising but incomplete
candidate. The public DTS package has strong time/depth/temperature metadata,
and public reports/papers show that pressure, flow, and temperature forcing
streams existed during the huff-and-puff test. I have not located the public
row-level Liberty/Pason forcing file for the August 26–30, 2025 interval.

For that reason, the FORGE August 2025 status is:

> `source-request-needed`

That means the dataset is worth pursuing, but it is not yet fit-ready for a
permeability calculation.

## What Is Not Claimed

This packet does not claim:

- FORGE August 2025 permeability has been estimated;
- FORGE pressure, flow, and DTS are already source-confirmed aligned;
- a specific fracture, flow zone, or reservoir permeability has been confirmed;
- the full thermal-recovery method has been validated across datasets;
- the materials here are a final manuscript or peer-reviewed study.

## Why The FORGE Request Is Narrow

The FORGE request is not a broad request for private project data. It is a
targeted request for the row-level forcing stream needed to decide whether the
public DTS record can be used responsibly.

Minimum useful information would include:

- timestamp convention and timezone;
- pressure, flow, injection-temperature, and 16B temperature rows for August
  26–30, 2025;
- units and channel definitions;
- whether the rows are Liberty or Pason source;
- whether values are raw or processed;
- enough overlap with the DTS HDF5 interval to test alignment.

If only a header and a short representative excerpt can be shared, that is still
useful for deciding whether the candidate is fit-ready or remains blocked.

## Packet Contents

- [`proof_example_egs_collab_exp2.md`](proof_example_egs_collab_exp2.md) — one sanitized proof example.
- [`forge_aug2025_request_rationale.md`](forge_aug2025_request_rationale.md) — why the FORGE row-level forcing data
  matter.
- [`evidence_discipline.md`](evidence_discipline.md) — how source-confirmed, assumption-labeled, and
  blocked claims are separated.
- [`sources_checked.md`](sources_checked.md) — public sources used in this packet.
- [`contact_and_citation.md`](contact_and_citation.md) — contact and reuse guidance.
- [`artifacts/`](artifacts/) — small static artifacts only; no raw datasets.

## Reuse Boundary

This repository is a preliminary research-progress packet. Unless otherwise
stated, all rights are reserved. Please contact the author before reusing text,
figures, or derived analysis.
