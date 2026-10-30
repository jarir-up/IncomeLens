# ADR-0018: Rules before models for extraction

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-009, carried forward)

## Context
Deterministic parsing is cheaper, testable and auditable.

## Decision
Per-format deterministic parsers, then a rule classifier. Only ambiguous rows go to a model with schema-constrained output, a confidence value and an explicit unclassified option. Low-confidence rows go to review; corrections become evaluation data.

## Consequences
Model calls stay rare and redacted.
