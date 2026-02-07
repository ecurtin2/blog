## Pulumi infra (Python + uv)

This directory manages the existing AWS setup for **`evancurtin.com`**:
- Route 53 hosted zone + records
- S3 bucket origin
- CloudFront distribution
- GitHub Actions deploy role (assumed via OIDC)

### Local usage

```bash
cd infra
uv sync

# Pulumi uses a local secrets manager by default; this repo uses a dummy
# passphrase for development. Use something stronger for real use.
export PULUMI_CONFIG_PASSPHRASE="dummy"

uv run pulumi login --local
uv run pulumi stack select dev || uv run pulumi stack init dev
uv run pulumi up
```

### GitHub Actions deploy

The deploy workflow expects a repo secret:
- **`AWS_ROLE_ARN`**: the role ARN output by Pulumi (`githubActionsRoleArn`)

