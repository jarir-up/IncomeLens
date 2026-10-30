# ADR-0016: Local embedding and reranking models

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-006/007, carried forward)

## Context
Offline, free and reproducible evaluation in CI.

## Decision
Use a local open embedding model and a local cross-encoder reranker. Exact models and licences are verified when added.

## Consequences
Retrieval ablations run without API cost.
