# 01: Wire fast and slow checks for the Python stack

**What to build:** `scripts/check.sh` runs ruff, ruff format, mypy, pytest and a package build through uv, and CI runs it after installing uv.

**Blocked by:** None (can start immediately).

**Status:** ready-for-agent

- [ ] `./scripts/check.sh` passes on a clean tree
- [ ] `./scripts/check.sh --fast` fails when a lint error is introduced
- [ ] CI workflow installs uv and Python 3.12 before running the script
- [ ] The run-the-app row in AGENTS.md stays unset (no runnable app yet)
