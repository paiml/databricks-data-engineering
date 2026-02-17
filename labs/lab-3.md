# Lab 3: Streaming with DLT

## Objectives

- Understand the difference between batch and streaming ingestion
- Use Auto Loader (cloudFiles) for incremental file processing
- Work with schema inference and explicit schema definitions
- Create streaming tables in DLT pipelines

## Prerequisites

- Completed [Lab 1](lab-1.md) and [Lab 2](lab-2.md)
- A running Databricks workspace with a volume configured

## Background

Batch processing reads all data every time a pipeline runs. Streaming processes only new data that has arrived since the last run. In Databricks, streaming is powered by Structured Streaming and Auto Loader.

**Key differences:**
- `spark.read` — Batch: reads everything
- `spark.readStream` — Streaming: reads only new data
- Auto Loader (`cloudFiles` format) — Streaming with automatic schema inference

## Exercise 1: Batch vs Streaming

Review [`examples/streaming/streaming_transformation.py`](../examples/streaming/streaming_transformation.py).

This file defines two tables:
1. `customers_batch` — Uses `spark.read` (batch)
2. `customers_streaming` — Uses `spark.readStream` with Auto Loader

### Questions

1. What happens if you run the batch pipeline twice with the same data?
2. What happens if you run the streaming pipeline twice with the same data?
3. Why does the streaming version use `cloudFiles.inferColumnTypes`?

## Exercise 2: Set Up Streaming Data

1. In your Databricks workspace, create a volume under your catalog/schema
2. Upload a CSV file with columns: `id`, `name`, `amount`
3. Create a DLT pipeline using the streaming example
4. Run the pipeline and verify the initial data loads

> **Path note:** Update the path `/Volumes/workspace/default/streaming` in the example to match your workspace volume location.

### Simulate New Data Arrival

1. Upload a second CSV file to the same volume directory
2. Re-run the pipeline
3. Observe that only the new file is processed by the streaming table
4. Compare row counts between the batch and streaming tables

## Exercise 3: Schema Challenges

When working with streaming data, schema management is important:

1. **Explicit schema** — You define the schema upfront with `StructType`
2. **Auto-inferred schema** — Auto Loader infers the schema from the data

### Tasks

1. Try removing the `cloudFiles.inferColumnTypes` option — what happens?
2. Add a new CSV file with an extra column — how does Auto Loader handle it?
3. What are the trade-offs between explicit and inferred schemas?

## Exercise 4: Streaming in the Wine Pipeline

Review the bronze layer of the wine pricing inventory:
[`examples/wine-pricing-inventory/bronze.py`](../examples/wine-pricing-inventory/bronze.py)

This pipeline uses both patterns:
- `bronze_wines` — Batch ingestion of the initial wine catalog
- `bronze_price_updates` — Streaming ingestion of price update files

### Questions

1. Why is the initial wine catalog loaded as batch rather than streaming?
2. How does the `ingestion_time` column help with auditing?
3. If a price update file is malformed, what happens to the pipeline?

## Key Takeaways

- Use `spark.read` for batch (full reprocessing) and `spark.readStream` for incremental processing
- Auto Loader (`cloudFiles`) handles new file detection automatically
- `cloudFiles.inferColumnTypes` is essential for proper type inference
- Prefer defining schemas explicitly in production for predictable behavior
- Streaming tables only process new data on each pipeline run
