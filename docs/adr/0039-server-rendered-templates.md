# ADR-0039: One set of server-rendered Jinja2 templates for both surfaces

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
ADR-0025 planned an API-first app with a thin demo UI. The checklist site is now public-facing and must build as static files (ADR-0030), and the local app needs real screens for the vault, row review, draft approval and export.

## Decision
Both surfaces use the same Jinja2 templates, with no JavaScript framework. CI renders the checklist to static files; the local app serves the templates from FastAPI. Adds Jinja2 as a dependency.

## Consequences
One component set and one design system for both surfaces. Rich client-side interaction costs extra and must justify itself. Supersedes ADR-0025.
