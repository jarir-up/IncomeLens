# 00 Wire scripts/check.sh

Serves: all goals (the gate everything else passes through).

Fill `FAST` and `SLOW` in `scripts/check.sh` for the approved stack (ADR-0013): ruff and mypy as fast checks; pytest and a build or import check as slow. Add the Python setup step to `.github/workflows/gates.yml`. Done when CI passes on a trivial PR and fails when a lint error is introduced.
