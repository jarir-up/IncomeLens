# ADR-0032: v0 local app ships as docker compose; packaging revisited after first release

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
The first users are developers (ADR-0002). A non-developer installer is a large build, and choosing it before anyone uses the app means guessing.

## Decision
The v0 local app runs with `docker compose`. Packaging for non-developers, and whether the local app needs Postgres or can use SQLite, are decided after the first local release.

## Consequences
Non-developer applicants cannot run v0 unaided. Keep the local database access behind SQLAlchemy so a later switch to SQLite stays cheap.
