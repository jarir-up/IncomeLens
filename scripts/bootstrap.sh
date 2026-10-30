#!/usr/bin/env bash
# One-time setup. Moves the agent harness (settings, hooks, Matt Pocock skills
# pinned at mattpocock/skills@a496f55) into .claude/ and the CI gates into
# .github/, then initialises git.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p .claude
cp -rn bootstrap/claude/. .claude/
mkdir -p .github
cp -rn bootstrap/github/. .github/
rm -rf bootstrap
chmod +x scripts/check.sh .claude/hooks/*.sh
[ -d .git ] || git init -q
echo "Harness installed. Next: open Claude Code here and run /grill-with-docs."
