# Lab 6: End-to-End Application

## Objectives

- Build a complete medallion architecture pipeline from scratch
- Combine batch and streaming ingestion in a single pipeline
- Implement Change Data Capture (CDC) with SCD Type 1 and Type 2
- Understand production pipeline organization and naming conventions

## Prerequisites

- Completed all previous labs
- Wine pricing data and price update CSV files uploaded to your volumes
- A running Databricks workspace

## Background

This lab brings together all the concepts from the course into a real-world wine pricing and inventory management system. The pipeline:

1. **Ingests** wine catalog data (batch) and price updates (streaming)
2. **Cleans** and validates data with expectations
3. **Tracks** price changes using Slowly Changing Dimensions (SCD)

### What is Change Data Capture (CDC)?

CDC tracks changes to data over time. DLT provides `apply_changes()` for this:

- **SCD Type 1** — Keeps only the latest value (overwrites history)
- **SCD Type 2** — Maintains full history with validity timestamps

## Exercise 1: Set Up the Data

1. Upload `wine-prices.csv` to `/Volumes/<catalog>/<schema>/raw/inventory/`
2. Create a `price_updates/` subdirectory in the same location
3. Upload one or more price update CSV files with columns: `wine_name`, `price`, `effective_date`

Example price update file:
```csv
wine_name,price,effective_date
Chateau Margaux,299.99,2024-06-01
Opus One,349.99,2024-06-01
```

## Exercise 2: Deploy the Full Pipeline

The wine pricing inventory pipeline consists of three files:
- [`examples/wine-pricing-inventory/bronze.py`](../examples/wine-pricing-inventory/bronze.py) — Ingestion
- [`examples/wine-pricing-inventory/silver.py`](../examples/wine-pricing-inventory/silver.py) — Cleaning
- [`examples/wine-pricing-inventory/gold.py`](../examples/wine-pricing-inventory/gold.py) — CDC and aggregation

### Tasks

1. Update all file paths to match your volume configuration
2. Create a new DLT pipeline and add all three files
3. Configure the pipeline with a target catalog and schema
4. Run the pipeline and examine the dependency graph

### What to Observe

- The graph shows both batch and streaming source tables
- Bronze tables feed into silver tables
- Silver price updates feed into both gold tables (SCD Type 1 and Type 2)

## Exercise 3: Understand CDC with apply_changes()

Review [`examples/wine-pricing-inventory/gold.py`](../examples/wine-pricing-inventory/gold.py).

```python
dlt.apply_changes(
    target="gold_current_prices",
    source="silver_price_updates",
    keys=["name"],
    sequence_by="effective_date",
    stored_as_scd_type=1
)
```

### Questions

1. What does `keys=["name"]` mean in the context of CDC?
2. What does `sequence_by="effective_date"` control?
3. What is the difference between the `gold_current_prices` and `gold_price_history` tables after multiple price updates?

## Exercise 4: Simulate Price Changes

1. After the initial pipeline run, upload a new price update CSV file to the `price_updates/` directory
2. Re-run the pipeline
3. Query `gold_current_prices` — do you see the updated prices?
4. Query `gold_price_history` — do you see both the old and new prices with validity dates?

### Verification Queries

```sql
-- Check current prices
SELECT * FROM your_catalog.your_schema.gold_current_prices ORDER BY name;

-- Check price history
SELECT * FROM your_catalog.your_schema.gold_price_history ORDER BY name, effective_date;
```

## Exercise 5: Production Considerations

Review the course material on production pipeline organization:

1. **File organization** — Group related transformations (bronze.py, silver.py, gold.py)
2. **Naming conventions** — Use consistent prefixes (bronze_, silver_, gold_)
3. **Storage locations** — Separate raw data from production tables
4. **Error handling** — Use `expect_or_fail` for critical data, `expect_or_drop` for recoverable issues

### Tasks

1. What would you change if this pipeline needed to handle multiple wine suppliers?
2. How would you add a fourth layer for executive dashboards?
3. What monitoring would you add for a production deployment?

## Key Takeaways

- A production pipeline combines batch and streaming in a single DLT pipeline
- `apply_changes()` enables CDC without writing complex merge logic
- SCD Type 1 keeps current values; SCD Type 2 maintains full history
- Consistent naming conventions and file organization are critical at scale
- The medallion architecture provides a clear data lineage from raw to business-ready
