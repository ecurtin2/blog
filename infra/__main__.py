import json

import pulumi
import pulumi_aws as aws


def require(cfg: pulumi.Config, key: str, default: str) -> str:
    return cfg.get(key) or default


cfg = pulumi.Config()

domain = require(cfg, "domain", "evancurtin.com")
hosted_zone_id = require(cfg, "hostedZoneId", "ZEV84TRNG5CSH")
bucket_name = require(cfg, "bucketName", "evancurtin.com")
distribution_id = require(cfg, "distributionId", "E4M8LUR5RBKVK")
certificate_arn = require(
    cfg,
    "certificateArn",
    "arn:aws:acm:us-east-1:627026565044:certificate/3cee70b1-7ce1-493a-a9b5-2fcd85572ba4",
)
github_repo = require(cfg, "githubRepo", "ecurtin2/blog")
enable_oac = cfg.get_bool("enableOac") or False
enable_uri_rewrite = cfg.get_bool("enableUriRewrite") or True

# Existing ACM validation record (already in Route 53).
acm_validation_name = require(
    cfg,
    "acmValidationRecordName",
    "_c6aaaa76f5a2d84dcc47900d83db0089.evancurtin.com.",
)
acm_validation_value = require(
    cfg,
    "acmValidationRecordValue",
    "_a8fd81fa320152ed7b6d6066413b87f4.tljzshvwok.acm-validations.aws.",
)

# Route 53 alias target for CloudFront (CloudFront hosted zone ID is fixed).
cloudfront_domain_name = require(cfg, "cloudfrontDomainName", "d3h3kt8ilbknqz.cloudfront.net.")
cloudfront_hosted_zone_id = require(cfg, "cloudfrontHostedZoneId", "Z2FDTNDATAQYW2")

# Providers
useast1 = aws.Provider("useast1", region="us-east-1")

# Data for IAM ARNs
caller = aws.get_caller_identity()
partition = aws.get_partition()


# --- Route 53 ---
zone = aws.route53.Zone(
    "evancurtinZone",
    name=f"{domain}.",
    comment="HostedZone created by Route53 Registrar",
    force_destroy=False,
    opts=pulumi.ResourceOptions(import_=hosted_zone_id),
)

apex_a_record_import_id = f"{hosted_zone_id}_{domain}._A"
apex_a = aws.route53.Record(
    "apexA",
    zone_id=zone.zone_id,
    name=f"{domain}.",
    type="A",
    aliases=[
        aws.route53.RecordAliasArgs(
            name=cloudfront_domain_name,
            zone_id=cloudfront_hosted_zone_id,
            evaluate_target_health=False,
        )
    ],
    opts=pulumi.ResourceOptions(import_=apex_a_record_import_id),
)

acm_validation_import_id = f"{hosted_zone_id}_{acm_validation_name}_CNAME"
acm_validation_record = aws.route53.Record(
    "acmValidationRecord",
    zone_id=zone.zone_id,
    name=acm_validation_name,
    type="CNAME",
    ttl=300,
    records=[acm_validation_value],
    opts=pulumi.ResourceOptions(import_=acm_validation_import_id),
)


# --- S3 ---
bucket = aws.s3.Bucket(
    "siteBucket",
    bucket=bucket_name,
    website=aws.s3.BucketWebsiteArgs(
        index_document="index.html",
        error_document="error.html",
    ),
    opts=pulumi.ResourceOptions(import_=bucket_name),
)


# --- ACM (us-east-1 for CloudFront) ---
certificate = aws.acm.Certificate(
    "siteCertificate",
    domain_name=domain,
    subject_alternative_names=[f"*.{domain}"],
    validation_method="DNS",
    opts=pulumi.ResourceOptions(import_=certificate_arn, provider=useast1),
)


# --- CloudFront ---
oac = None
oac_id: str | None = None
if enable_oac:
    oac = aws.cloudfront.OriginAccessControl(
        "siteOac",
        name=f"{domain}-oac",
        description=f"OAC for {domain} CloudFront -> S3",
        origin_access_control_origin_type="s3",
        signing_behavior="always",
        signing_protocol="sigv4",
    )
    oac_id = oac.id

# Rewrite /blog -> /blog/ and /blog/ -> /blog/index.html (and normalize //).
uri_rewrite_fn = None
if enable_uri_rewrite:
    uri_rewrite_fn = aws.cloudfront.Function(
        "uriRewriteFunction",
        name="evancurtin-com-uri-rewrite",
        runtime="cloudfront-js-1.0",
        publish=True,
        code="""function handler(event) {
  var request = event.request;
  var uri = request.uri || "/";

  // Normalize multiple slashes.
  var normalized = uri.replace(/\\/{2,}/g, "/");
  if (normalized !== uri) {
    return {
      statusCode: 301,
      statusDescription: "Moved Permanently",
      headers: { location: { value: normalized } }
    };
  }

  // If path has no extension and doesn't end with '/', redirect to add trailing slash.
  var hasExtension = uri.lastIndexOf(".") > uri.lastIndexOf("/");
  if (!hasExtension && !uri.endsWith("/")) {
    return {
      statusCode: 301,
      statusDescription: "Moved Permanently",
      headers: { location: { value: uri + "/" } }
    };
  }

  // If directory path, rewrite to index.html.
  if (uri.endsWith("/")) {
    request.uri = uri + "index.html";
  }

  return request;
}
""",
    )

distribution = aws.cloudfront.Distribution(
    "siteDistribution",
    enabled=True,
    is_ipv6_enabled=True,
    price_class="PriceClass_All",
    http_version="http2",
    aliases=[domain],
    default_root_object="index.html",
    origins=[
        aws.cloudfront.DistributionOriginArgs(
            **(
                {
                    "origin_id": f"S3-{bucket_name}",
                    "domain_name": f"{bucket_name}.s3.amazonaws.com",
                    "s3_origin_config": aws.cloudfront.DistributionOriginS3OriginConfigArgs(
                        origin_access_identity="",
                    ),
                    "connection_attempts": 3,
                    "connection_timeout": 10,
                }
                | ({"origin_access_control_id": oac_id} if enable_oac else {})
            )
        )
    ],
    default_cache_behavior=aws.cloudfront.DistributionDefaultCacheBehaviorArgs(
        target_origin_id=f"S3-{bucket_name}",
        viewer_protocol_policy="redirect-to-https",
        allowed_methods=["GET", "HEAD"],
        cached_methods=["GET", "HEAD"],
        compress=False,
        function_associations=(
            [
                aws.cloudfront.DistributionDefaultCacheBehaviorFunctionAssociationArgs(
                    event_type="viewer-request",
                    function_arn=uri_rewrite_fn.arn,
                )
            ]
            if uri_rewrite_fn is not None
            else []
        ),
        forwarded_values=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesArgs(
            query_string=False,
            cookies=aws.cloudfront.DistributionDefaultCacheBehaviorForwardedValuesCookiesArgs(
                forward="none"
            ),
        ),
        min_ttl=0,
        default_ttl=60,
        max_ttl=31536000,
    ),
    restrictions=aws.cloudfront.DistributionRestrictionsArgs(
        geo_restriction=aws.cloudfront.DistributionRestrictionsGeoRestrictionArgs(
            restriction_type="none",
        )
    ),
    viewer_certificate=aws.cloudfront.DistributionViewerCertificateArgs(
        acm_certificate_arn=certificate.arn,
        ssl_support_method="sni-only",
        minimum_protocol_version="TLSv1.1_2016",
    ),
    opts=pulumi.ResourceOptions(import_=distribution_id),
)


# --- Lock down S3 to CloudFront (only when OAC enabled) ---
if enable_oac:
    public_access_block = aws.s3.BucketPublicAccessBlock(
        "siteBucketPublicAccessBlock",
        bucket=bucket.id,
        block_public_acls=True,
        ignore_public_acls=True,
        block_public_policy=True,
        restrict_public_buckets=True,
    )

    distribution_arn = f"arn:{partition.partition}:cloudfront::{caller.account_id}:distribution/{distribution_id}"

    policy_doc = pulumi.Output.all(bucket.arn).apply(
        lambda args: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "AllowCloudFrontServicePrincipalReadOnly",
                        "Effect": "Allow",
                        "Principal": {"Service": "cloudfront.amazonaws.com"},
                        "Action": ["s3:GetObject"],
                        "Resource": f"{args[0]}/*",
                        "Condition": {"StringEquals": {"AWS:SourceArn": distribution_arn}},
                    }
                ],
            }
        )
    )

    bucket_policy = aws.s3.BucketPolicy(
        "siteBucketPolicy",
        bucket=bucket.id,
        policy=policy_doc,
        opts=pulumi.ResourceOptions(depends_on=[public_access_block, distribution]),
    )


# --- GitHub Actions OIDC + deploy role ---
# Note: this account already has a shared GitHub OIDC provider. We reference it
# rather than trying to manage it (to avoid state conflicts across Pulumi stacks).
github_oidc_provider_arn = require(
    cfg,
    "githubOidcProviderArn",
    f"arn:{partition.partition}:iam::{caller.account_id}:oidc-provider/token.actions.githubusercontent.com",
)
github_oidc_provider = aws.iam.get_open_id_connect_provider(arn=github_oidc_provider_arn)

deploy_role = aws.iam.Role(
    "githubActionsDeployRole",
    name="github-actions-blog-deploy",
    assume_role_policy=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {"Federated": github_oidc_provider.arn},
                    "Action": "sts:AssumeRoleWithWebIdentity",
                    "Condition": {
                        "StringEquals": {"token.actions.githubusercontent.com:aud": "sts.amazonaws.com"},
                        "StringLike": {
                            "token.actions.githubusercontent.com:sub": [
                                f"repo:{github_repo}:ref:refs/heads/master",
                                f"repo:{github_repo}:ref:refs/heads/main",
                            ]
                        },
                    },
                }
            ],
        }
    ),
)

deploy_policy = aws.iam.Policy(
    "githubActionsDeployPolicy",
    name="github-actions-blog-deploy",
    policy=pulumi.Output.all(bucket.arn).apply(
        lambda args: json.dumps(
            {
                "Version": "2012-10-17",
                "Statement": [
                    {
                        "Sid": "S3Sync",
                        "Effect": "Allow",
                        "Action": [
                            "s3:ListBucket",
                            "s3:GetBucketLocation",
                        ],
                        "Resource": [args[0]],
                    },
                    {
                        "Sid": "S3ObjectRW",
                        "Effect": "Allow",
                        "Action": [
                            "s3:GetObject",
                            "s3:PutObject",
                            "s3:DeleteObject",
                        ],
                        "Resource": [f"{args[0]}/*"],
                    },
                    {
                        "Sid": "CloudFrontInvalidation",
                        "Effect": "Allow",
                        "Action": ["cloudfront:CreateInvalidation"],
                        "Resource": [
                            f"arn:{partition.partition}:cloudfront::{caller.account_id}:distribution/{distribution_id}"
                        ],
                    },
                ],
            }
        )
    ),
)

aws.iam.RolePolicyAttachment(
    "githubActionsDeployPolicyAttachment",
    role=deploy_role.name,
    policy_arn=deploy_policy.arn,
)


pulumi.export("domain", domain)
pulumi.export("hostedZoneId", zone.zone_id)
pulumi.export("bucketName", bucket.bucket)
pulumi.export("cloudFrontDistributionId", distribution.id)
pulumi.export("githubActionsRoleArn", deploy_role.arn)

