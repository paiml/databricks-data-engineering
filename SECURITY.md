# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please report it by:

1. **Do not** open a public GitHub issue
2. Email security concerns to the maintainers
3. Include details about the vulnerability
4. Allow time for a fix before public disclosure

## Security Considerations

This repository contains educational examples for building data pipelines with Databricks. When using these examples:

- **Workspace Credentials**: Never commit Databricks tokens or credentials to version control
- **Data Paths**: Review volume paths before running pipelines to avoid accessing unintended data
- **Access Controls**: Use Databricks workspace permissions to restrict access to sensitive data
- **Network Security**: Configure network access rules for your Databricks workspace

## Best Practices

1. Use environment variables or Databricks secrets for sensitive configuration
2. Review data access permissions before sharing pipelines
3. Keep Databricks runtime and dependencies updated
4. Use Unity Catalog for fine-grained access control
