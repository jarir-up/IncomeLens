#!/usr/bin/env bash
# PostToolUse hook: fast checks after every file edit.
# Exit 2 sends stderr back to Claude so it fixes the failure in its next step.
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
if ! ./scripts/check.sh --fast; then
  echo "Fast checks failed after your edit. Fix the cause before continuing." >&2
  exit 2
fi
exit 0
