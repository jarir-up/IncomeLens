# ADR-0020: Custom evaluation harness

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-011, carried forward)

## Context
Deterministic metrics first; model judging only where code can't check.

## Decision
A pytest-based harness for deterministic metrics, an LLM judge only for faithfulness, calibrated against hand labels. Golden sets are versioned in the repo.

## Consequences
A RAG-metrics library may cross-check, never replace.
