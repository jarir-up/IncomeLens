# 06: One-page dossier, end-to-end command and CI

**What to build:** one command runs the whole path, writes a one-page dossier ordered like the checklist with the figure cited to its rows, and prints per-stage evaluation; CI runs it against a Postgres service.

**Blocked by:** 03, 05.

**Status:** ready-for-agent

- [ ] Command exits non-zero if any stage's evaluation fails
- [ ] Dossier cites every figure it shows
- [ ] CI workflow runs the command
