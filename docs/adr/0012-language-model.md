# ADR-0012: Language model: Claude primary, local model for ambiguous rows

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
IncomeLens ADR-005 (changed by owner 2026-10-07) chose Llama 3.1 8B via Ollama for the MVP, with a hosted model only after deployment and peer testing. On 2026-10-29 the owner accepted Claude as primary with a local model optional.

## Decision
Claude extracts requirements from public sources and drafts letters. A local model classifies ambiguous transaction rows so applicant text can stay on the machine. Drafts are written with placeholders for figures and names (for example `{{figure:total_income_12m}}`, `{{name:sponsor}}`), and local code fills them in, so Claude never sees the applicant's figures or names. Model IDs live in configuration.

## Consequences
ADR-0017 (numbers rule) holds by construction for drafts. Supersedes IncomeLens ADR-005.
