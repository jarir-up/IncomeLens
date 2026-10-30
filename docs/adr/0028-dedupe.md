# ADR-0028: Idempotent ingestion and deduplication

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-019, carried forward)

## Context
The same transaction appears in overlapping exports.

## Decision
Stable key from source, account and external transaction ID where present; otherwise a deterministic fingerprint. Files dedupe by sha256. Ambiguous candidates are flagged, never dropped silently.

## Consequences
Dedupe precision and recall are metrics.
