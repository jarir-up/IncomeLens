# ADR-0017: The language model never produces figures

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-008, carried forward)

## Context
Wrong financial figures are an unacceptable error class.

## Decision
Figures come only from parameterised SQL functions. A verifier rejects any number in output that is not in tool output. No free-form text-to-SQL.

## Consequences
Enforced by R-20.
