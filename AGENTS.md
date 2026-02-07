## How to work in this repo (for AI agents)

This repo is a Hugo site with a small Python toolchain (managed by `uv`) and AWS infra managed by Pulumi.

### Golden rule: use `just`

Prefer `just` recipes over ad-hoc commands. The `justfile` is the source of truth for how to:
- install tooling
- convert notebooks
- run the dev server
- build for production
- build the resume

Key recipes:
- **Bootstrap**: `just install`
- **Dev** (convert + serve): `just dev`
- **Build** (convert + minify): `just publish`
- **Build only**: `just build`
- **Convert notebooks only**: `just convert`
- **Resume**: `just resume` (or `just resume-pdf`, `just resume-docx`)

### Local dependencies

`just install` ensures:
- **Hugo extended v0.140.2** (keep in sync with GitHub Actions)
- `uv`
- `typst`

Python dependencies are installed via **`uv sync`** (see `pyproject.toml` / `uv.lock`).

### Content model

- Blog posts live under `content/blog/<slug>/index.md` and typically include:
  - frontmatter (YAML)
  - optional `teaser_image` (used on list pages)
- Notebook-backed posts:
  - author in `notebooks/*.ipynb` + matching `notebooks/*.yml`
  - generate Hugo bundles with `just convert` (runs `convert-notebooks.py`)

### Preview and build output

- Dev server: `just serve` (or `just dev` to include conversion)
- Production output directory: `public/`

Avoid committing build outputs like `public/`, `resources/_gen/`, or ad-hoc build folders (for example `hugo-build-test/`).

### Deploy (GitHub Actions)

Workflows live in `.github/workflows/`:
- **PRs**: build-only
- **Push to `master`/`main`**: build + deploy to S3 + CloudFront invalidation

No long-lived AWS keys are used. Deployment uses **GitHub OIDC** and expects this repo secret:
- **`AWS_ROLE_ARN`**: IAM role ARN to assume for deploy

### Infra (Pulumi)

Pulumi project is in `infra/` (Python + uv).

Common commands:

```bash
cd infra
uv sync
export PULUMI_CONFIG_PASSPHRASE="dummy"
uv run pulumi login --local
uv run pulumi stack select dev || uv run pulumi stack init dev
uv run pulumi preview
uv run pulumi up
```

Notes:
- CloudFront uses **OAC** and the origin bucket is **private**.
- A CloudFront Function normalizes `//` URLs and rewrites directory paths like `/blog/` → `/blog/index.html`.

### “Do not”

- Don’t introduce Docker-based workflows (this repo prefers `uv` + `just`).
- Don’t add AWS access keys to the repo or GitHub secrets.
- Don’t commit generated artifacts (resume build folders, Hugo build directories, etc.) unless explicitly requested.

