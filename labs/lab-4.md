# Lab 4: Bronze Layer Fundamentals

## Objectives

- Understand the medallion architecture and its three layers
- Design bronze layer ingestion pipelines
- Ingest raw data from volumes into delta tables
- Apply bronze layer best practices (no transformation, preserve raw data)

## Prerequisites

- Completed [Lab 1](lab-1.md) through [Lab 3](lab-3.md)
- A running Databricks workspace with data uploaded to volumes

## Background

The **medallion architecture** organizes data into three quality layers:

| Layer | Purpose | Data Quality |
|-------|---------|-------------|
| **Bronze** | Landing zone for raw data | As-is from source |
| **Silver** | Cleaned and normalized | Validated and deduplicated |
| **Gold** | Business-ready aggregations | Business logic applied |

The bronze layer is the foundation. Its job is simple: ingest raw data without modification. All transformation happens downstream in the silver and gold layers.

### Why No Transformation in Bronze?

- Preserves the original data for debugging and auditing
- Allows reprocessing if business rules change
- Separates concerns: ingestion vs. transformation

## Exercise 1: Upload Data to Volumes

1. In your Databricks workspace, navigate to your catalog/schema
2. Create a volume named `raw` (if not already created)
3. Upload the wine ratings CSV file to the volume
4. Verify the file is accessible at your volume path

## Exercise 2: Create a Bronze Table

Review [`examples/simple-pipeline/bronze.py`](../examples/simple-pipeline/bronze.py).

The `wine_bronze` function reads a CSV file directly:

```python
@dlt.table(
    name="wine_bronze",
    comment="Raw wine data ingested from volume"
)
def wine_bronze():
    return spark.read.csv(
        "/Volumes/workspace/default/raw/wine-ratings.csv",
        header=True, inferSchema=True, escape='"'
    )
```

### Tasks

1. Update the path to match your volume location
2. Create a DLT pipeline with this file
3. Run the pipeline and examine the bronze table
4. Check the column types — are they what you expected?
5. Look for data quality issues (nulls, special characters, duplicates)

## Exercise 3: Bronze with Metadata

Review [`examples/wine-pricing-inventory/bronze.py`](../examples/wine-pricing-inventory/bronze.py).

This version adds an `ingestion_time` column and drops a problematic index column:

```python
.drop("_c0")
.withColumn("ingestion_time", current_timestamp())
```

### Questions

1. Why is adding `ingestion_time` acceptable in the bronze layer (even though we said "no transformation")?
2. What is the `_c0` column and why is it dropped?
3. How would you handle a CSV that has no header row?

## Exercise 4: Design Bronze Ingestion

For a new data source (e.g., application logs in JSON format), design a bronze ingestion pipeline:

1. What `spark.read` format would you use?
2. What options would you set?
3. Would you use batch or streaming ingestion?
4. What metadata columns would you add?

## Key Takeaways

- The bronze layer is a landing zone — keep data as close to raw as possible
- Adding metadata (ingestion timestamps) is an acceptable bronze-layer addition
- Use `inferSchema=True` for exploration, but define schemas explicitly in production
- Upload source files to Databricks Volumes for easy access
- The bronze table preserves the full history for downstream reprocessing
