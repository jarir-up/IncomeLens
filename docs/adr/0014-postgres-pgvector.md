# ADR-0014: Postgres with pgvector and full-text search

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-003, carried forward)

## Context
One store gives SQL, vectors, full-text search and transactions together; the corpus is small.

## Decision
Postgres with pgvector and built-in full-text search. Hybrid retrieval fuses results in one query layer.

## Consequences
A dedicated vector database is a documented migration path, not a need.
