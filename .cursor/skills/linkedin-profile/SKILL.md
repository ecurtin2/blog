---
name: linkedin-profile
description: Generates a complete LinkedIn profile (headline, About, experience, projects, publications, skills) from `data/profile.toml` and the voice rules in `style_guide.md`. Use when the user asks to draft/update their LinkedIn profile, headline, About section, experience bullets, or LinkedIn summary.
---

# LinkedIn Profile

Generate a paste-ready LinkedIn profile that is fully grounded in:
- `data/profile.toml` (facts, roles, highlights)
- `style_guide.md` (voice and writing rules)

If the user asks for a “LinkedIn profile” without extra constraints, produce a default profile and keep everything within common LinkedIn limits.

## Inputs (always)

1. Read `data/profile.toml`
2. Read `style_guide.md`

## Optional inputs (use when provided)

- Target role(s), industry, or audience (recruiter vs peer vs founder)
- Keywords to emphasize (must still be true)
- Tight length constraints (e.g., “About <= 1,200 chars”)
- “Actively interviewing” vs “not looking”

## Output format (default)

Return a single markdown document with these sections, each written to be copy/pasteable into LinkedIn:

- Headline
- About
- Featured (links)
- Experience (company entries with role(s) + bullets)
- Education
- Publications (selected)
- Projects (selected)
- Skills (top set)

Do not include phone number or email unless the user explicitly requests it.
Write in first-person voice (LinkedIn-native), while keeping the tone direct and grounded.

## Content selection rules

- Prefer items where `included_in` contains `"resume"` or `"site"`.
- If an item has `included_in = []`, treat it as “exclude by default”.
- Do not invent roles, dates, metrics, employers, or claims not present in `data/profile.toml` / `style_guide.md`.
- You may rewrite phrasing for clarity and LinkedIn fit, while keeping claims semantically identical.

## Voice + writing rules (hard requirements)

Apply `style_guide.md` directly:
- No hype, no theatrics, no “thought leadership” language.
- Lead with outcomes and impact, not activity.
- Describe systems, not tasks.
- Include scale/context/constraints when relevant.
- Prefer concrete verbs (built, shipped, designed, reduced).
- Treat evaluation and production behavior as first-class themes.
- Cut anything that doesn’t change the reader’s understanding.

## Generation workflow

1. Extract from `data/profile.toml`:
   - `bio.tagline`, `bio.expanded`, and (if useful) `bio.identity.whoami`
   - Experience entries + highlights (group multi-role companies into a single company section)
   - Skills groups (filter using `included_in`)
   - Education, publications, and projects

2. Draft the profile:
   - **Headline**: short, specific, outcome-oriented. Prefer a single line that says what you do + where you’re strong + domain context.
   - **About**: 3–6 short paragraphs. Include (a) what you build, (b) how you work (evaluation + production feedback), (c) domain context (high-stakes / regulated), (d) a concrete “what people rely on me for” sentence.
   - **Experience**: for each role/company, write 3–6 bullets from `highlights`, rewritten to be tighter and more system/outcome-oriented. Keep numbers and scope.
   - **Featured / Projects / Publications**: choose a small set; prefer those with URLs and crisp one-line descriptions.
   - **Skills**: output a “Top skills” list (roughly 30–50). Keep it concrete and aligned to the profile narrative.

3. Run a style QA pass (before final):
   - Remove inflated verbs (“spearheaded”, “leveraged”, “synergized”).
   - Ensure each bullet has an outcome or measurable effect (or a clear system-level result).
   - Ensure claims are grounded in the TOML.
   - Ensure it sounds like a calm builder, not marketing copy.

## Defaults when the user doesn’t specify

- Audience: recruiter + hiring manager
- Target roles: applied scientist / ML engineer (LLM systems)
- Length: keep **Headline** concise; keep **About** compact and skimmable

## Template to follow

Use this template (fill in content; keep tone and constraints):

```markdown
## Headline
[one line]

## About
[short paragraphs]

## Featured
- [Title] — [URL] — [one-line why it matters]

## Experience
### [Company] — [Location]
**[Title 1]** ([Start] – [End])
- [bullet]
- [bullet]

**[Title 2]** ([Start] – [End])
- [bullet]

### [Company] — [Location]
**[Title]** ([Start] – [End])
- [bullet]

## Education
- [Degree] — [Institution]

## Publications (selected)
- [Authors]. “[Title].” [Venue], [Year]. DOI: [doi]

## Projects (selected)
- [Name] — [URL] — [one-line description]

## Skills (top)
[comma-separated or bulleted list]
```

## Examples (how users will ask)

- “Generate my full LinkedIn profile from `data/profile.toml`.”
- “Rewrite my LinkedIn **About** to be tighter and more grounded (<= 1,200 chars).”
- “Draft LinkedIn experience bullets for my Relativity roles; keep it outcomes-first and include evaluation + scale.”
- “Tailor my LinkedIn profile for applied scientist roles focused on LLM evaluation and reliability.”

