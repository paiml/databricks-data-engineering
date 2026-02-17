# Examples

Pipeline examples for each module of the Data Engineering with Databricks course.

> **Note on paths:** All examples reference `/Volumes/workspace/default/` for data paths. You must update these paths to match your own Databricks workspace and volume configuration.

## Directory Structure

| Directory | Description | Course Lesson |
|-----------|-------------|---------------|
| `dlt-basics/` | SQL-based Bronze-Silver-Gold pipeline | 1.1 DLT Foundations |
| `streaming/` | Batch vs streaming ingestion with Auto Loader | 1.3 Streaming with DLT |
| `simple-pipeline/` | Wine ratings pipeline (Bronze, Silver, Gold) | 2.1–2.3 Medallion Architecture |
| `wine-pricing-inventory/` | End-to-end inventory system with CDC | 3.1 End-to-End Application |

## Running Examples

These files are designed to run as **Delta Live Table pipelines** in Databricks:

1. Upload the Python or SQL file to your Databricks workspace
2. Create a new DLT pipeline from the **Workflows > Delta Live Tables** section
3. Point the pipeline to your uploaded file
4. Configure the target catalog and schema
5. Run the pipeline

For multi-file pipelines (like `simple-pipeline/` or `wine-pricing-inventory/`), add all files from the directory to the same pipeline configuration.
