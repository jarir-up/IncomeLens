# ADR-0015: LangGraph for the agent; retrieval as plain code

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-004, carried forward)

## Context
The readiness agent needs state, tools and an approval interrupt; retrieval must stay transparent and tunable.

## Decision
LangGraph for the agent graph. Retrieval and checks are plain, testable Python and SQL.

## Consequences
Framework lock-in is limited to the readiness module.
