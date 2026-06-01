# Method basis: Purwamaska and Fulton 2026

This repository screens public datasets around a simple idea from Purwamaska and Fulton 2026: after fluid circulation disturbs borehole temperatures, the way the
borehole warms back toward background temperature can contain information about
where the surrounding rock is more permeable.

The paper is:

> Purwamaska, I., & Fulton, P. M. (2026). Borehole thermal recovery as a method
> for quantifying subsurface permeability. *Geochemistry, Geophysics,
> Geosystems*, 27, e2025GC012508. https://doi.org/10.1029/2025GC012508

Article page:

- https://www.scienceopen.com/document?vid=a77faaf4-85c3-4dcf-b1ee-7a99b7c6f46a

Supporting model/data archive:

- https://zenodo.org/records/16895640

## The idea in plain language

Water circulation cools or warms the borehole and nearby rock. After circulation
stops, the temperature does not instantly return to normal. It recovers over
time.

If a depth interval is more permeable, more fluid can move into or through that
part of the formation during circulation. That fluid movement changes how heat
is stored and transported. As a result, the temperature recovery curve can look
different at permeable zones than at tight zones.

The Purwamaska and Fulton 2026 paper uses physics simulations of heat and fluid flow to connect
that recovery behavior to permeability and permeable-zone geometry.

## What this repo borrows from that method

This repository borrows the evidence structure, not the exact full model:

1. identify a temperature recovery window after circulation or pump stop;
2. fit a simple recovery descriptor such as `tau`;
3. use source-backed pressure, flow, timing, and geometry assumptions to define
   the forcing;
4. convert the forcing into a bulk/model-equivalent permeability scale in `m²`;
5. compare that scale against published permeability context when available;
6. label unresolved or assumption-heavy routes honestly.

The screening catalog applies this structure across a small public-dataset
demonstration set. The included Brady/PoroTomo example is the current verified/qualified
threshold-compatible route, not a reproduction of every Purwamaska and Fulton
2026 model simulation.

## What this repo does not claim

This repository does not claim that the active public routes are the same field
setting as the Purwamaska and Fulton 2026 paper. It also does not claim measured
rock permeability, exact-fracture permeability, exhaustive geothermal coverage,
or universal validation of the method.

The narrower claim is:

> Public geothermal temperature-recovery records can be screened through an
> evidence ladder to decide which routes support claim-bounded
> bulk/model-equivalent permeability estimates in `m²`, and which routes remain
> discovery-only, source-request-needed, metadata-limited, or support-only.
