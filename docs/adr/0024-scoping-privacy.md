# ADR-0024: Per-person scoping and PII redaction

- Status: Superseded by ADR-0035
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-015, carried forward)

## Context
Applicant and sponsor data must not mix; logs must not leak personal data.

## Decision
Every record is scoped to its person. Personal data is redacted from logs and traces.

## Consequences
Postgres row-level security may be unnecessary under local-first (Q-6).
