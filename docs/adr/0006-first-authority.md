# ADR-0006: First data: Germany, Italy, France; study first

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
The registry needs a first slice of real data. These three missions have consulates in Karachi as well as embassies in Islamabad.

## Decision
Load Germany, Italy and France first. Purposes: study (national long-stay) first, then tourism, business (client visit), conference and family visit. Include exit-side Pakistani requirements that apply.

## Consequences
Study visas are national D visas, not Schengen C visas, so the registry must model both (Q-11). Other missions load through the same pipeline.
