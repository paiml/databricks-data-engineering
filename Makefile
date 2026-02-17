# Makefile for databricks-data-engineering
# Use 'uv' for all Python operations

.PHONY: all install test lint format coverage clean help

# Default Python/uv commands
PYTHON := uv run python
RUFF := uv run ruff
PYTEST := uv run pytest

# Default target
all: lint test

# Install dependencies
install:
	@echo "=== Installing dependencies ==="
	uv sync --all-extras

# Run all tests
test:
	@echo "=== Running tests ==="
	$(PYTEST) tests/ -v

# Run linting
lint:
	@echo "=== Running linter ==="
	$(RUFF) check examples/ --ignore E501,E722

# Format code
format:
	@echo "=== Formatting code ==="
	$(RUFF) format examples/
	$(RUFF) check examples/ --fix --ignore E501,E722

# Run tests with coverage
coverage:
	@echo "=== Running tests with coverage ==="
	$(PYTEST) tests/ --cov=examples --cov-report=term-missing --cov-report=html

# Validate Python syntax in all examples
validate:
	@echo "=== Validating Python syntax ==="
	$(PYTHON) -m py_compile examples/**/*.py

# Clean build artifacts
clean:
	@echo "=== Cleaning build artifacts ==="
	rm -rf __pycache__ .pytest_cache .coverage htmlcov .mypy_cache .ruff_cache
	rm -rf build dist *.egg-info
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true

# Help
help:
	@echo "Available targets:"
	@echo "  install    - Install dependencies with uv"
	@echo "  test       - Run all tests"
	@echo "  lint       - Run linter"
	@echo "  format     - Format code"
	@echo "  coverage   - Run tests with coverage"
	@echo "  validate   - Validate Python syntax"
	@echo "  clean      - Clean build artifacts"
	@echo "  help       - Show this help"
