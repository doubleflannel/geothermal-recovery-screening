# Dataset route catalog

This page is a compact public status catalog for the thermal-recovery screening
program. The working tracker is maintained separately in a live Google Sheet:

<https://docs.google.com/spreadsheets/d/1clQ9oGVqPozfUQeIbLHMBUPvhqqskDtSy330f_75nVY>

The spreadsheet is the current editable ledger. This Markdown page is the
repo-safe summary: no private notes, no raw unpublished rows, and no unresolved
route is treated as a permeability result.

## Status labels used here

- `Validated / qualified`: thermal-recovery estimate has an independent
  published permeability-scale comparison, but caveats still apply.
- `Discovery-only`: public rows and metadata support a defensible estimate, but
  no independent numeric permeability comparator is available yet.
- `Source-request-needed`: sources suggest the missing stream exists, but the
  needed rows or metadata have not been located publicly.
- `Metadata limitation`: the route is useful as a claim-boundary example, but
  timing, channel definitions, or alignment metadata are not strong enough for a
  permeability result.
- `Support-only`: useful hydraulic or context evidence, but not a counted
  Purwamaska and Fulton 2026-style thermal-recovery case.

## Counted thermal-recovery routes

| Route | Status | Public-facing result | Boundary |
| --- | --- | --- | --- |
| Brady/PoroTomo 56-1 cold-slug DTS | Validated / qualified | Central `7.35e-14 m²`; broad uncertainty band. | Qualified same-field fault-scale support, not exact outflow-patch validation. |
| DEMO-FTES Test 1 hot-water circulation | Discovery-only | Central `2.59e-15 m²`; uncertainty band from assumed bridge. | Needs Test 1-specific comparator before validation. |
| DEMO-FTES Test 1 ambient circulation | Discovery-only | Central `5.79e-15 m²`; uncertainty band from assumed bridge. | Needs phase-specific pressure/drop and comparator tightening. |
| Bedretto HM-1d / BULGG interval 8 | Discovery-only | Central `7.37e-15 m²`; warmback bridge. | Top-temperature proxy, not source-confirmed full-interval rock recovery. |
| SLS TH4 warm-back figure route | Discovery-only | Central `3.07e-12 m²`; figure-digitized warmback bridge. | Figure-only until row-level DTS and forcing rows are available. |
| Campbell/AGES cold-water channel-geometry lookup | Discovery-only | Central `1.10e-12 m²`; geometry-dominated band. | Channel/fracture geometry is assumption-labeled. |
| Cranfield SECARB CO₂ thermal-front route | Discovery-only | Selected `1.71e-14 m²`; broad thermal-front bridge range. | Pressure/tracer/ERT support the sequence, not exact numeric validation. |
| LSU PERTT Jan 2020 borehole recovery | Discovery-only | Central `3.93e-14 m²`; preferred `2.15e-14–8.84e-14 m²`. | Exact annulus geometry is applied; independent model-resistance comparator is still missing. |
| Choutuppal H+ hot/cold-water tests | Discovery-only | Figure-level bridge around `1.4e-11 m²`. | Exact April 2019 CH03/CH12 pressure/head rows are still missing. |
| OSU GDR 1770 thermohydraulic fracture-flow loop | Discovery-only lab case | H2O small fracture `1.36e-06 m²`; H2O large fracture `3.36e-06 m²`. | Lab fracture-slot result, not field reservoir permeability. |

## Below-threshold controls

| Route | Status | Public-facing result | Boundary |
| --- | --- | --- | --- |
| EGS Collab Exp2 AMU 34 m recovery crop | Validated / qualified below-threshold control | Preferred `1.59e-15 m²`; source-constrained band `3.52e-16–4.40e-15 m²`. | Useful non-cherry-picking control, but below the approximate `1e-14 m²` Purwamaska-Fulton effective range and not a headline threshold-compatible proof. |

## Source-request-needed routes

These routes are not counted as permeability results. They have enough public
context to justify a narrow request for missing rows or metadata.

| Route | Needed item | Decision it would unblock |
| --- | --- | --- |
| DEMO-FTES comparator route | Test 1 phase-specific permeability, transmissivity, aperture, or conductance comparator. | Whether DEMO hot-water and ambient estimates can become validated / qualified. |
| SLS TH4 | Row-level DTS plus synchronized pressure, flow, injected-water temperature, timezone, and flowmeter comparison rows. | Whether the figure-only route becomes row-level fit-ready. |
| Soultz/CDGP | Restricted hydraulic-temperature CSVs or representative samples with timestamps, pressure, flow, temperature, units, and interval metadata. | Whether Soultz can become a fit-ready P/F route. |
| Newberry 2012 Dec 7 | Original DTS interpretation files, inlet/pump-water temperature, active-flow interval, and thermal model bridge. | Whether Dec 7 is a real P/F fit or remains blocked. |
| Raft River April 2015 RRG-9 ST1 | Raw falloff pressure/time rows and paired pre-shut-in injection rate/WHP/surface temperature rows. | Whether the published falloff comparator can be independently reconstructed. |
| Raft River long-term RRG-9 injectivity | Long-term pressure/rate/temperature rows, pressure-drop definition, and source-supported geometry. | Whether injectivity change can be converted to defensible `m²`. |
| HE-53 2009 flow-test DTS | Row-level same-window flow/WHP/wellhead-temperature forcing and feed-zone metadata. | Whether HE-53 can become a P/F thermal route instead of figure/table support. |
| Groß Schönebeck active-depth DTS | Sept. 8–9 2011 DTS/logging rows, surface flow, ESP drawdown, bottom-hole pressure, spinner rows, and calibration/depth metadata. | Whether active-depth production logging can become a P/F thermal route. |
| Utah FORGE Aug 2025 16B DTS | Aug. 26–30 Liberty/Pason pressure, flow, temperature rows and channel/timing metadata. | Whether the strong public DTS package can become fit-ready. |

## Metadata-limitation routes

| Route | Why it stays out of the count |
| --- | --- |
| Utah FORGE 2024 Pason/PLT/DTS | Public sources do not source-confirm enough Pason time/channel definitions or PLT clock convention for fixed timing alignment. It is useful as a metadata-discipline example, not a permeability result. |

## Support-only routes

| Route | Why it is support-only |
| --- | --- |
| Newberry 2014 October falloff | Hydraulic reconstruction can reproduce a published pressure-transient scale, but it is not a thermal-recovery route without a thermal-profile-to-`m²` bridge. |
| Pressure-flow, falloff, transmissivity, and productivity-index routes | These can be useful appendix checks, but they do not count as Purwamaska and Fulton 2026-style thermal-recovery evidence unless a raw temperature recovery and thermal-to-`m²` bridge are added. |

## How to read this catalog

A route can be scientifically useful without being validated. The main paper
idea is thermal recovery mapped to bulk/model-equivalent permeability. If public
rows support that mapping, the route can be labeled discovery-only. If an
independent comparator later appears, it can be upgraded to validated / qualified
with the comparison tier stated explicitly.
