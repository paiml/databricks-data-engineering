# Lab 2: Data Quality with Expectations

## Objectives

- Understand the three expectation violation actions: warn, drop, and fail
- Implement expectations in DLT pipelines
- Diagnose data quality issues using the pipeline UI
- Choose the right violation action for different scenarios

## Prerequisites

- Completed [Lab 1](lab-1.md)
- A running Databricks workspace

## Background

Data quality is critical in production pipelines. DLT expectations let you define constraints on your data and choose what happens when those constraints are violated:

| Action | Behavior | Use Case |
|--------|----------|----------|
| `EXPECT` (warn) | Records pass through, violations are logged | Monitoring quality trends |
| `EXPECT ... ON VIOLATION DROP ROW` | Invalid records are silently removed | Cleaning known bad data |
| `EXPECT ... ON VIOLATION FAIL` | Pipeline fails immediately | Critical data that must be valid |

## Exercise 1: Understanding Violation Actions

Review the SQL pipeline in [`examples/dlt-basics/my_transformation.sql`](../examples/dlt-basics/my_transformation.sql).

The silver layer defines two constraints:
```sql
CONSTRAINT valid_email EXPECT (email IS NOT NULL) ON VIOLATION DROP ROW
CONSTRAINT valid_age EXPECT (age > 0) ON VIOLATION DROP ROW
```

### Questions

1. If you changed `valid_email` to use `FAIL` instead of `DROP ROW`, what would happen?
2. If you changed `valid_age` to use `EXPECT` only (warn), would Charlie's record appear in the gold layer?
3. When would you choose `FAIL` over `DROP ROW` in a production pipeline?

## Exercise 2: Expectations in Python

Review the bronze pipeline in [`examples/simple-pipeline/bronze.py`](../examples/simple-pipeline/bronze.py).

The silver layer uses the Python decorator:
```python
@dlt.expect_or_drop("valid_rating", "rating IS NOT NULL")
```

### Tasks

1. Run this pipeline in your Databricks workspace with wine ratings data
2. Check the pipeline graph — how many records were dropped?
3. Click on the silver table and look at the **Data Quality** tab
4. Note the percentage of records that passed vs. failed the expectation

## Exercise 3: Multiple Expectations

The wine pricing inventory pipeline uses different violation strategies for different tables. Review:
- [`examples/wine-pricing-inventory/silver.py`](../examples/wine-pricing-inventory/silver.py)

### Questions

1. Why does `silver_wines` use `expect_or_drop` while `silver_price_updates` uses `expect_or_fail`?
2. What is the business justification for failing the entire pipeline on invalid price updates?
3. How would you add an expectation to ensure wine ratings are between 80 and 100?

## Exercise 4: Design Your Own Expectations

For a hypothetical e-commerce dataset with columns `order_id`, `customer_email`, `amount`, `status`, design expectations for the silver layer:

1. Which columns should use `DROP ROW`?
2. Which columns should use `FAIL`?
3. Which columns should use `EXPECT` (warn only)?

Write the SQL or Python constraints and explain your reasoning.

## Key Takeaways

- Expectations define data quality rules directly in your pipeline code
- Three violation actions give you flexibility for different scenarios
- Use `warn` for monitoring, `drop` for cleaning, `fail` for critical data
- The pipeline UI shows diagnostic details about expectation violations
- Multiple expectations can be applied to the same table
