# ADR-0029: Distribution-shift splits and agent isolation from test data

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-024, carried forward)

## Context
Generated data plus iterative tuning invites leakage, and coding agents are a leakage path.

## Decision
Dev and test splits differ in templates, layouts and instances. Frozen test and adversarial data are readable only by the harness. If test results influence a change, regenerate the test split.

## Consequences
Enforced by R-26.
