#!/bin/bash
# Scaffold a new Agent Skill

set -e

SKILL_NAME="$1"

if [ -z "$SKILL_NAME" ]; then
    echo "Usage: bash scaffold.sh <skill-name>"
    echo "Example: bash scaffold.sh deploy-app"
    exit 1
fi

# Validate skill name (lowercase, numbers, hyphens only)
if ! [[ "$SKILL_NAME" =~ ^[a-z0-9-]+$ ]]; then
    echo "Error: Skill name must contain only lowercase letters, numbers, and hyphens."
    exit 1
fi

SKILL_DIR=".cursor/skills/$SKILL_NAME"

if [ -d "$SKILL_DIR" ]; then
    echo "Error: Skill '$SKILL_NAME' already exists at $SKILL_DIR"
    exit 1
fi

echo "Creating skill: $SKILL_NAME"

# Create directory structure
mkdir -p "$SKILL_DIR"

# Create SKILL.md template
cat > "$SKILL_DIR/SKILL.md" << EOF
---
name: $SKILL_NAME
description: TODO - Describe what this skill does and when to use it.
---

# ${SKILL_NAME//-/ }

TODO - Brief overview of this skill.

## When to Use

- TODO - When is this skill relevant?

## Instructions

TODO - Step-by-step guidance for the agent.

1. First step
2. Second step
EOF

echo "✓ Created $SKILL_DIR/SKILL.md"
echo ""
echo "Next steps:"
echo "  1. Edit $SKILL_DIR/SKILL.md with your skill's instructions"
echo "  2. Add scripts/ directory if you need executable code"
echo "  3. Add references/ directory for additional documentation"
echo "  4. Restart Cursor or check Settings → Rules to verify"
