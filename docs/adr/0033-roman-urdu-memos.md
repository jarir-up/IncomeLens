# ADR-0033: English interface; the classifier handles Roman Urdu memos

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
ADR-0026 kept everything in English. Real statement memos contain Roman Urdu, so an English-only classifier misreads real data.

## Decision
UI, docs and queries stay in English. The rule classifier's keyword lists include common Roman Urdu memo terms, and part of the synthetic memos in evaluation sets are in Roman Urdu.

## Consequences
Classification metrics cover Roman Urdu memos. Supersedes ADR-0026.
