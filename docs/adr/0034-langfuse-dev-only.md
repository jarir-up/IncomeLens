# ADR-0034: Langfuse in development and CI only

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
ADR-0019 self-hosts Langfuse. Running it inside the applicant's local app is heavy and adds a place personal data could collect.

## Decision
Self-hosted Langfuse is used in development and CI. The applicant's local app has no tracing.

## Consequences
No traces exist on applicant machines, so none can leak. Bugs reported by applicants are reproduced with synthetic data. Supersedes ADR-0019.
