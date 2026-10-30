# PRD — PakkiFile

Owner: Muhammad Jariruddin · Last updated: 2026-10-30

## Problem

Pakistani freelancers with real, steady foreign income are refused, delayed or priced out of opportunities that depend on proof of income and standing: visas, rentals, bank finance and cards, mortgages, subscriptions, government schemes, tax and registration status, admissions. The cause is rarely a lack of money or qualifications. Their papers don't tell one consistent, checkable story in the form each reviewing authority expects, and no local source tells them what each authority actually requires, which items are mandatory, conditional or optional, and how sure anyone is about that.

What it costs them today: lost fees, agent and lawyer fees, weeks of compiling, a refusal on record that must be declared in later applications, and missed trips, studies and client work.

The failures fall into six kinds of mismatch (see `GLOSSARY.md`): format, continuity, identity, classification, legitimacy and rule conflict.

## Users

| ID | User | The one job | Version |
|---|---|---|---|
| U1 | Applicant (freelancer) | Know what this application needs from someone like me, see what's missing or contradictory, and assemble one true file | v0 |
| U3 | Contributor | Add or correct a requirement, with its source | v0 |
| U4 | Sponsor | Supply funds evidence that holds up | v0 inside the applicant's file; own user later |
| U5 | Counterparty (client) | Issue a confirmation letter quickly | v0 as a letter request the applicant sends |
| U6 | Reviewing officer | Judge the file fast | v0 as the reader the dossier is designed for; not a user |
| U7 | Maintainer | Resolve flagged registry conflicts and moderate contributions | v0 |
| U2 | Consultant or lawyer | Compile files for many clients | Later |
| U8 | Researcher or policy body | Use anonymised aggregates | Later |
| U9 | Community or association | Distribute to members | Later |

## Goals

- **G-1** For each loaded authority, application and applicant profile, produce a requirements checklist where every item is typed (mandatory, conditional, optional), cites an official source and carries a computed confidence.
- **G-2** Keep the registry current without manual research: changes at official sources are detected and re-extracted automatically; people review only conflicts and low-confidence items.
- **G-3** Detect every mismatch kind (M1 to M6) between an applicant's evidence and the requirements, and between the evidence items themselves.
- **G-4** Export a dossier the reviewing officer can judge quickly, where every figure traces to a page of a source document.
- **G-5** Personal documents never leave the applicant's machine, except redacted snippets sent to a language model.
- **G-6** Prove the model generalises by loading a second authority class after Schengen.

## Non-goals

- Moving or holding money; benefits, insurance or contribution routing.
- Booking appointments or applying on anyone's behalf.
- Predicting approval or refusal, or giving legal, immigration or tax conclusions.
- Editing, generating or "fixing" official documents. PakkiFile compiles and annotates; it never alters evidence.
- Suggesting how to hide or work around a mismatch.
- Hosting or storing anyone's personal documents.
- Monetisation or a pitch line in v0.
- Consultant multi-client workspaces (U2) in v0.

## Requirements

### Registry (MVP)
- **FR-1** The registry models Authority × Application × Applicant profile; Schengen is its first data, not its shape.
- **FR-2** Each requirement records its type, any condition that triggers it, its source (document, section, URL), the date retrieved and the date last verified.
- **FR-3** Confidence is computed from source authority, recency and agreement across sources, never entered by hand.
- **FR-4** Official source documents are fetched, checksummed and re-extracted when they change.
- **FR-5** Conflicting or low-confidence requirements go to a review queue; everything else publishes without manual review.
- **FR-6** First data: Germany, Italy and France; purposes study (national long-stay), tourism, business, conference and family visit.
- **FR-7** The registry includes exit-side Pakistani requirements where they apply (for example Protector of Emigrants clearance).
- **FR-8** Community refusal and approval stories are stored as a separate, lower-authority layer that can lower or raise confidence but never override an official source.
- **FR-9** A hosted checklist page serves the registry and holds no personal data.

### Evidence vault (MVP, local)
- **FR-10** Ingest statements as CSV and PDF, including password-protected PDFs, plus ePRC and S-PRC certificates, FBR returns, invoices and contracts.
- **FR-11** Classify transactions with rules first; send only ambiguous rows to a language model; flag what stays uncertain instead of guessing.
- **FR-12** Compute every figure with SQL. The language model never produces a number.
- **FR-13** Every computed figure links to the source rows and document pages it came from.

### Mismatch engine (MVP, local)
- **FR-14** Check evidence against the applicable requirements and report each gap with the requirement it fails.
- **FR-15** Check evidence items against each other (for example statement totals against ePRC totals and the tax return) and report contradictions.
- **FR-16** Label every finding with its mismatch kind (M1 to M6), and state the risk truthfully without suggesting concealment.

### Readiness and dossier (MVP, local)
- **FR-17** Given a target application, plan the work, run the checks, and draft supporting letters: income explanation, sponsor letter and a client confirmation request.
- **FR-18** Nothing is exported until the applicant approves each draft.
- **FR-19** Export an indexed dossier ordered for the reviewing officer, with every figure cited.

### Later
- **FR-20** A second authority class (bank finance, rental or another visa family).
- **FR-21** Opt-in outcome reports (approved or refused, with stated reasons) feeding confidence and the evaluation set.
- **FR-22** Consultant workspaces (U2).

## Success measures

- Missions covered, and the share of requirements re-verified within the last 90 days.
- Checklists generated and dossiers exported, counted only through opt-in pings.
- Opt-in outcome reports received.
- Evaluation scores: requirement-extraction accuracy against hand-labelled checklists; mismatch-detection precision and recall on seeded synthetic cases; zero figures not traceable to SQL.
- GitHub stars, read as a distribution signal only.

## Open questions

Owned by the owner, to settle in `/grill-with-docs`. Agents don't resolve these. The list lives under "Waiting on owner" in `docs/PROGRESS.md`.

Settled 2026-10-30: language model (ADR-0012), licence (ADR-0031), local packaging for v0 (ADR-0032), Roman Urdu memos (ADR-0033).
