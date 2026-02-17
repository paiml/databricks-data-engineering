# Capstone Project: Build Your Own Data Pipeline

## Overview

Build a complete medallion architecture pipeline using Delta Live Tables on the Databricks FREE edition. This project brings together all concepts from the course: DLT pipelines, expectations, streaming, bronze/silver/gold layers, and Change Data Capture.

## Requirements

Choose a dataset and build a production-style pipeline with the following components:

### 1. Bronze Layer — Data Ingestion

- Ingest at least one batch data source into a bronze table
- Ingest at least one streaming data source using Auto Loader
- Add ingestion metadata (timestamp, source file name)
- Store raw data without transformation

### 2. Silver Layer — Data Cleaning

- Clean and normalize the bronze data
- Apply at least 3 DLT expectations with appropriate violation actions
- Handle nulls, duplicates, and data type issues
- Select only the columns needed for downstream use

### 3. Gold Layer — Business Logic

- Create at least 2 gold tables for different business use cases
- Apply aggregations, filters, or derived columns
- Implement at least one CDC table using `apply_changes()` with SCD Type 1 or Type 2
- Optimize at least one gold table with Z-ordering

### 4. Pipeline Organization

- Organize code into separate files: `bronze.py`, `silver.py`, `gold.py`
- Use consistent naming conventions (bronze_, silver_, gold_ prefixes)
- Add comments explaining each table's purpose
- Document any path assumptions

## Suggested Datasets

You may use any dataset you like. Here are some suggestions that work well with the FREE Databricks edition:

| Dataset | Batch Source | Streaming Source |
|---------|-------------|-----------------|
| Weather data | Historical observations CSV | Daily forecast updates |
| Stock prices | Historical prices CSV | Intraday price updates |
| Product inventory | Product catalog CSV | Order/restock updates |
| Server logs | Historical log dump | New log files arriving |

## Project Structure

```
capstone/
├── bronze.py          # Bronze layer ingestion
├── silver.py          # Silver layer cleaning and validation
├── gold.py            # Gold layer business logic and CDC
└── README.md          # Documentation (see below)
```

## Documentation Requirements

Your `README.md` should include:

1. **Dataset description** — What data are you working with?
2. **Pipeline architecture** — Diagram or description of your bronze → silver → gold flow
3. **Expectations** — List of data quality rules and why you chose each violation action
4. **Gold tables** — Description of each gold table and its business use case
5. **Setup instructions** — How to upload data and configure paths in your workspace
6. **Lessons learned** — What challenges did you encounter and how did you solve them?

## Evaluation Criteria

| Category | Points | What We Look For |
|----------|--------|-----------------|
| **Bronze Layer** | 20 | Correct batch + streaming ingestion, metadata columns |
| **Silver Layer** | 25 | Proper cleaning, 3+ expectations with justified violation actions |
| **Gold Layer** | 25 | Business-ready tables, aggregations, CDC implementation |
| **Organization** | 15 | Clean file structure, naming conventions, comments |
| **Documentation** | 15 | Clear README with architecture and setup instructions |
| **Total** | **100** | |

## Bonus Challenges

- **Multi-source merge** (+5) — Combine data from 2+ different source formats (CSV, JSON, Parquet)
- **Dashboard** (+5) — Create a Databricks SQL dashboard from your gold tables
- **Alerting** (+5) — Configure pipeline alerts for expectation failures
- **Parameterized pipeline** (+5) — Use pipeline configuration parameters for paths and thresholds

## Getting Started

1. Review the course examples in [`examples/wine-pricing-inventory/`](../examples/wine-pricing-inventory/) as a reference implementation
2. Choose your dataset and plan your bronze/silver/gold tables
3. Start with a single bronze table and build outward
4. Test each layer independently before connecting them
5. Add expectations and CDC last, after the basic flow works

## Tips

- Use the FREE Databricks Community Edition — all features needed for this project are available
- Start simple and iterate — get a basic pipeline working before adding complexity
- Test expectations with intentionally bad data to verify they work
- Use `DESCRIBE DETAIL` to verify Z-order optimization took effect
- Keep your data files small for faster iteration during development
