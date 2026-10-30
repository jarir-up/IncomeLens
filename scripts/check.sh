#!/usr/bin/env bash
# Single entry point for every check. Agents, hooks and CI all call this,
# so "it passed" means the same thing everywhere.
#   ./scripts/check.sh          lint, types, tests, build
#   ./scripts/check.sh --fast   lint and types only (runs after every edit)
set -uo pipefail
cd "$(dirname "$0")/.."

# Fill these in for this project's stack (the first issue), e.g.
#   FAST=("npm run lint" "npx tsc --noEmit")
#   SLOW=("npm test" "npm run build")
FAST=()
SLOW=()

if [ ${#FAST[@]} -eq 0 ] && [ ${#SLOW[@]} -eq 0 ]; then
  echo "scripts/check.sh has no checks configured yet. Wiring them up is the first issue." >&2
  # Unconfigured checks must never pass CI silently.
  if [ "${CI:-}" = "true" ]; then exit 1; fi
  exit 0
fi

commands=("${FAST[@]}")
if [ "${1:-}" != "--fast" ]; then commands+=("${SLOW[@]}"); fi

failed=0
for cmd in "${commands[@]}"; do
  if ! output=$(bash -c "$cmd" 2>&1); then
    echo "FAILED: $cmd" >&2
    echo "$output" | tail -n 40 >&2
    failed=1
  fi
done
exit $failed
