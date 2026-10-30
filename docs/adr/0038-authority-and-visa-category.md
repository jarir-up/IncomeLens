# ADR-0038: Visa category belongs to the application; each mission is its own authority

- Status: Approved
- Approved by: Muhammad Jariruddin, 2026-10-30

## Context
Study visas are national long-stay (D) visas, not Schengen short-stay (C) visas, yet earlier docs called Schengen "the first authority". The registry must model both categories (ADR-0006).

## Decision
An authority is one institution, such as the German Embassy Islamabad or the Consulate General of Germany, Karachi. Visa category (C or D) is part of the application, so a German study visa (D) and a German tourist visa (C) are two applications at the same authority. An embassy and a consulate are two authorities that may cite the same source. Schengen missions are an authority class.

## Consequences
Checklists are keyed by the mission the applicant actually applies at. A source shared by two missions is stored once and cited by both.
