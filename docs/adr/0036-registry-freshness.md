# ADR-0036: Weekly fetch, text checksums, and a plain auto-publish rule

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
ADR-0007 left the fetch schedule and the auto-publish threshold open. Raw HTML changes on every fetch, and a numeric confidence threshold has nothing to calibrate against until extraction is evaluated.

## Decision
Sources are fetched weekly. A source counts as changed when the checksum of its normalised extracted text changes, not its raw bytes. A requirement publishes without review only if its top source is an official checklist or a consulate page, no source of equal or higher authority disagrees, and it was verified within the last 90 days. Everything else goes to review.

## Consequences
Fewer false changes. The rule is replaced by a confidence threshold once the extraction evaluation gives real numbers.
