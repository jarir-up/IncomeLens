# ADR-0041: The local app downloads the whole registry

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
If the local app requested one checklist at a time, host logs would show which application a given IP address is preparing.

## Decision
The local app downloads the whole registry as one file and selects the matching checklist on the applicant's machine. It never requests a single application from the server.

## Consequences
The host learns nothing about any applicant's target. The download grows with the registry; revisit only if it becomes slow.
