# ADR-0035: Per-person scoping in the local vault, without row-level security

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
ADR-0024 assumed a multi-tenant server, where Postgres row-level security separates users. Under local-first (ADR-0002) the vault holds one applicant plus their sponsors.

## Decision
Every vault record references its person (applicant or sponsor), and queries filter on it in one place. Personal data is redacted from logs. No Postgres row-level security.

## Consequences
Applicant and sponsor data stay separate without database policies. Supersedes ADR-0024.
