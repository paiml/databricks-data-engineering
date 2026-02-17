# Contributing to Data Engineering with Databricks

Thank you for your interest in contributing to this project!

## Getting Started

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/databricks-data-engineering.git
   cd databricks-data-engineering
   ```

3. Install dependencies:
   ```bash
   uv sync --all-extras
   ```

## Development Workflow

### Code Style

We use `ruff` for linting and formatting:

```bash
# Check code style
uv run ruff check examples/

# Format code
uv run ruff format examples/
```

### Adding Examples

When adding new examples:

1. Place files in the appropriate `examples/` subdirectory
2. Add comments explaining the pipeline and any path assumptions
3. Update the README if adding a new category

## Pull Request Process

1. Create a feature branch from `main`
2. Make your changes
3. Ensure linting passes
4. Update documentation as needed
5. Submit a pull request

## Code of Conduct

Please be respectful and constructive in all interactions.

## Questions?

Open an issue for any questions about contributing.
