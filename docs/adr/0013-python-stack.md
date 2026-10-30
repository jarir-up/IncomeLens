# ADR-0013: Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2, Alembic, uv, ruff, mypy, pytest

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-07 (IncomeLens ADR-002, carried forward)

## Context
Typed validation keeps model output schema-checked; the stack fits the problem.

## Decision
Use Python 3.12, FastAPI, Pydantic v2, SQLAlchemy 2 with Alembic, uv for dependencies, ruff and mypy for quality, pytest for tests.

## Consequences
Small, typed modules; tests first where they clarify design.
