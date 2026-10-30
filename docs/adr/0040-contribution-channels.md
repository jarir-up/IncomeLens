# ADR-0040: Contributions through pull requests and a structured issue form

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
Contributors correct requirements (U3) and applicants share community stories. A web form would make the hosted site receive data, against ADR-0002 and ADR-0030.

## Decision
Requirement corrections are pull requests on the registry data files, which are YAML, one file per application. Community stories come through a GitHub issue form with structured fields only: mission, application, month and year, outcome, stated reason, documents asked for. It has no free-text field for names or personal details. A maintainer turns each accepted story into a data file.

## Consequences
No data-receiving endpoint exists. Contributing needs a GitHub account.
