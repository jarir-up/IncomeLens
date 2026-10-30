#!/usr/bin/env bash
# Stop hook: full checks before Claude ends a turn with uncommitted changes.
# Exit 2 makes Claude keep working with the failure in front of it.
input=$(cat)
# Claude is already continuing because of this hook: let it stop rather than loop.
if echo "$input" | grep -Eq '"stop_hook_active"[[:space:]]*:[[:space:]]*true'; then
  exit 0
fi
cd "${CLAUDE_PROJECT_DIR:-.}" || exit 0
# Conversation-only turns change nothing, so there is nothing to check.
if [ -z "$(git status --porcelain 2>/dev/null)" ]; then
  exit 0
fi
if ! ./scripts/check.sh; then
  echo "Full checks fail with your uncommitted changes. Fix them, or record what broke in docs/PROGRESS.md." >&2
  exit 2
fi
exit 0
