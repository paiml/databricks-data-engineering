# Lab 1: DLT Foundations

## Objectives

- Understand what Delta Live Tables (DLT) are and how they differ from traditional Spark jobs
- Create your first DLT pipeline using SQL
- Explore the pipeline graph and execution model
- Understand the Bronze-Silver-Gold pattern at a high level

## Prerequisites

- A Databricks workspace (the FREE Community Edition works)
- Basic familiarity with SQL

## Background

Delta Live Tables provide a declarative approach to building ETL pipelines. Instead of writing imperative code that specifies *how* to process data, you declare *what* transformations you want, and Databricks manages the execution, dependency ordering, and error handling.

DLT pipelines are created from the **Workflows > Delta Live Tables** section in Databricks. The platform automatically builds a dependency graph from your table definitions and executes them in the correct order.

## Exercise 1: Explore the SQL Pipeline

Review the example file [`examples/dlt-basics/my_transformation.sql`](../examples/dlt-basics/my_transformation.sql).

This file defines three tables in a single pipeline:

1. **`customers_raw`** (Bronze) — Raw inline data with intentional quality issues
2. **`customers_clean`** (Silver) — Cleaned data with constraints applied
3. **`age_by_initial`** (Gold) — Aggregated business-ready data

### Questions

1. What happens to Bob's record in the silver layer? Why?
2. What happens to Charlie's record? Why?
3. How many records make it to the gold layer?

## Exercise 2: Create Your First DLT Pipeline

1. Log into your Databricks workspace
2. Navigate to **Workflows > Delta Live Tables**
3. Click **Create pipeline**
4. Upload or paste the SQL from `examples/dlt-basics/my_transformation.sql`
5. Configure a target catalog and schema (e.g., `workspace.default`)
6. Click **Start** to run the pipeline

### What to Observe

- The pipeline graph shows three connected tables
- Hover over each table to see record counts
- Notice how records are dropped between bronze and silver
- The gold layer contains the final aggregated result

## Exercise 3: Modify the Pipeline

Try these modifications to deepen your understanding:

1. Add a new customer with a valid email and age — does it appear in all three layers?
2. Change a constraint from `DROP ROW` to `FAIL` — what happens when invalid data is encountered?
3. Add a new gold table that counts customers by the first letter of their email domain

## Key Takeaways

- DLT pipelines can be written in SQL or Python
- `CREATE LIVE TABLE` defines a materialized view in the pipeline
- `EXPECT` constraints define data quality rules
- `ON VIOLATION DROP ROW` silently removes invalid records
- `LIVE.table_name` references other tables within the same pipeline
- Databricks manages the execution order automatically
