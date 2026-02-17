# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-17

### Added
- Complete data engineering course with 6 labs
- 4 example categories covering DLT, streaming, medallion architecture, and CDC
- Course outline and capstone project documentation
- Pipeline examples: SQL and Python DLT pipelines
- Wine ratings pipeline (simple Bronze-Silver-Gold)
- Wine pricing inventory pipeline (end-to-end with CDC)
- Streaming ingestion examples with Auto Loader

### Examples
- `dlt-basics/` - SQL-based Bronze-Silver-Gold pipeline
- `streaming/` - Batch vs streaming ingestion with Auto Loader
- `simple-pipeline/` - Wine ratings with full medallion layers
- `wine-pricing-inventory/` - End-to-end pipeline with Change Data Capture
