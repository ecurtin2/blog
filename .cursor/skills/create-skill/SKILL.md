---
name: create-skill
description: Create new Agent Skills for Cursor. Use when the user wants to create a skill, add agent capabilities, or automate workflows with skills.
---

# Create Skill

Create new Agent Skills that extend Cursor's capabilities with domain-specific knowledge and workflows.

## When to Use

- User wants to create a new skill
- User wants to automate a workflow with a skill
- User asks about making skills or agent capabilities
- User wants to package instructions for reuse

## Instructions

### 1. Gather Requirements

Ask the user:
- **What should the skill do?** Get a clear description of the task or workflow.
- **When should it be used?** Understand the triggers/context for the skill.
- **Should it auto-invoke or be manual?** Auto = agent decides when relevant. Manual = only via `/skill-name`.
- **Does it need scripts?** Determine if executable code is required.

### 2. Create the Skill Structure

Run the scaffolding script with the skill name:

```bash
bash .cursor/skills/create-skill/scripts/scaffold.sh <skill-name>
```

This creates:
```
.cursor/skills/<skill-name>/
├── SKILL.md
├── scripts/      (if needed)
├── references/   (if needed)
└── assets/       (if needed)
```

### 3. Write the SKILL.md

Follow this template:

```markdown
---
name: skill-name
description: Concise description of what this skill does and when to use it.
disable-model-invocation: false  # Set true for manual-only skills
---

# Skill Name

Brief overview of what this skill accomplishes.

## When to Use

- Bullet points describing when this skill is relevant
- Be specific about triggers and context

## Instructions

Step-by-step guidance for the agent:

1. First step
2. Second step
3. Continue with clear, actionable instructions

## Examples

Show example usage or expected outputs if helpful.
```

### 4. Best Practices

- **Name**: Use lowercase letters, numbers, and hyphens only. Must match folder name.
- **Description**: Be specific about WHEN to use, not just WHAT it does. This helps the agent decide relevance.
- **Instructions**: Write as if instructing a capable developer. Be clear and actionable.
- **Scripts**: Make them self-contained with good error messages.
- **Keep it focused**: One skill = one capability. Split complex workflows into multiple skills.
- **Progressive loading**: Put detailed docs in `references/` to keep main SKILL.md lean.

### 5. Skill Locations

| Location | Scope |
|----------|-------|
| `.cursor/skills/` | Project-level |
| `~/.cursor/skills/` | User-level (global) |

### 6. Testing

After creating, verify the skill appears in:
- Cursor Settings → Rules → Agent Decides section
- Or invoke manually with `/skill-name` in chat
