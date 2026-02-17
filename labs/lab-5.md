# Lab 5: Silver and Gold Layers

## Objectives

- Build silver layer tables with data cleaning and validation
- Apply expectations to enforce data quality in the silver layer
- Create gold layer tables with business logic and aggregations
- Understand incremental vs full recompute strategies
- Apply Z-order optimization to gold tables

## Prerequisites

- Completed [Lab 4](lab-4.md) with wine data loaded in a bronze table
- A running Databricks workspace

## Background

### Silver Layer
The silver layer transforms raw bronze data into clean, normalized tables. Common operations include:
- Removing nulls and duplicates
- Cleaning string data (removing special characters, trimming whitespace)
- Dropping unused columns
- Applying data quality expectations

### Gold Layer
The gold layer applies business logic to create purpose-built tables for specific use cases like reporting, analytics, or downstream applications.

## Exercise 1: Build the Silver Layer

Review the silver table in [`examples/simple-pipeline/bronze.py`](../examples/simple-pipeline/bronze.py) (the `wine_silver` function).

### Data Cleaning Operations

The silver layer performs several cleaning steps:
1. Removes carriage returns and newlines from text columns
2. Trims whitespace from string columns
3. Drops the unused `grape` column
4. Removes duplicate records
5. Drops records with null ratings

### Tasks

1. Run the full pipeline (bronze + silver) in your workspace
2. Compare record counts between bronze and silver
3. Click on the silver table in the pipeline graph and examine:
   - How many records were dropped by the `valid_rating` expectation?
   - What percentage of data passed quality checks?
4. Query the silver table and verify the text columns are cleaned

## Exercise 2: Build Gold Layer Tables

Review [`examples/simple-pipeline/gold_by_region.py`](../examples/simple-pipeline/gold_by_region.py).

This file creates two gold tables:
1. **`wine_gold_top_rated`** — All wines rated 90 or above
2. **`wine_gold_by_region`** — Aggregate counts and average ratings by region

### Tasks

1. Add this file to your existing pipeline
2. Run the pipeline and observe the full dependency graph (bronze → silver → gold)
3. Query `wine_gold_top_rated` — how many wines have a rating >= 90?
4. Query `wine_gold_by_region` — which region has the highest average rating?

## Exercise 3: Incremental Processing

When you re-run a pipeline:
- **Full recompute**: All tables are recalculated from scratch
- **Incremental**: Only new data is processed (for streaming tables)

### Tasks

1. Run your pipeline a second time without changing any data
2. Observe the execution time — is it faster than the first run?
3. Add a new row to your bronze source data and re-run
4. Check if the gold aggregations updated correctly

## Exercise 4: Optimizations

Databricks supports Z-order optimization for improving query performance on gold tables.

### Tasks

1. After your pipeline runs, execute in a SQL cell:
   ```sql
   DESCRIBE DETAIL your_catalog.your_schema.wine_gold_by_region
   ```
2. Note the file count and size
3. Apply Z-ordering:
   ```sql
   OPTIMIZE your_catalog.your_schema.wine_gold_by_region ZORDER BY (region)
   ```
4. Run `DESCRIBE DETAIL` again and compare the metrics

## Exercise 5: Silver Layer for Pricing Data

Review [`examples/wine-pricing-inventory/silver.py`](../examples/wine-pricing-inventory/silver.py).

### Questions

1. Why does `silver_wines` select only specific columns instead of using `SELECT *`?
2. What is the difference between `expect_or_drop` and `expect_or_fail`?
3. Why does `silver_price_updates` rename `wine_name` to `name`?

## Key Takeaways

- The silver layer is where data cleaning and validation happen
- Use `expect_or_drop` for non-critical quality issues, `expect_or_fail` for critical ones
- Gold tables apply business logic: filtering, aggregation, and derived metrics
- Streaming tables (`read_stream`) enable incremental processing
- Z-order optimization improves query performance on frequently filtered columns
- Each layer serves a specific purpose — don't skip layers
