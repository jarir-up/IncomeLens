# ADR-0007: Registry is machine-built with computed confidence

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
Researching and maintaining requirements by hand does not scale and makes the owner the bottleneck. Carries the principles of IncomeLens ADR-022 (source authority and conflict handling), approved 2026-10-07.

## Decision
The registry models Authority x Application x Applicant profile. A pipeline fetches official sources, detects changes, extracts typed requirements with citations, and computes confidence from source authority, recency and agreement. Entries above a threshold publish automatically; conflicts and low-confidence items go to a review queue. Equal-authority conflicts are shown with both citations. Community stories adjust confidence but never override an official source.

## Consequences
Humans review by exception. Extraction quality is gated by evaluation against hand-labelled checklists. Threshold and schedule pending (Q-8).
