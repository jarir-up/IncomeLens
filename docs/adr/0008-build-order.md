# ADR-0008: Build order with evaluation gates; one public v0 launch

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
Calendar releases paced for a large team don't fit a two-person build with coding agents. The real constraint is verification, not typing. Carries IncomeLens ADR-025 (tracer bullet first), approved 2026-10-07.

## Decision
Start with a tracer bullet through the whole path. Then build in dependency order, each step closing on an evaluation gate: registry, local vault, mismatch engine, readiness agent and dossier, then a second authority class. The hosted checklist deploys continuously as soon as the first mission passes its gate. One public v0 launch carries the rest.

## Consequences
No dates. Progress is measured by gates passed.
