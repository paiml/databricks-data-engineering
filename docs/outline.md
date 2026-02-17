# Data Engineering with Databricks — Course Outline

**Course Description**
Build production data pipelines using Delta Live Tables, Databricks Workflows, and the medallion architecture for reliable, scalable ETL.

**Learning Outcomes**
1. Design data pipelines using medallion architecture (bronze/silver/gold)
2. Build declarative ETL with Delta Live Tables and expectations
3. Orchestrate workflows with Databricks Jobs and dependencies
4. Implement Change Data Capture (CDC) and streaming ingestion

---

## Module 1: Delta Live Tables Fundamentals

### Lesson 1.1: DLT Foundations
- 1.1.0 Course introduction
- 1.1.1 Introduction
- 1.1.2 Introduction to Delta Live Tables
- 1.1.3 DLT syntax with Python and SQL
- 1.1.4 Creating your first DLT pipeline
- 1.1.5 Summary

**Lab:** [Lab 1 — DLT Foundations](../labs/lab-1.md)
**Examples:** [`examples/dlt-basics/`](../examples/dlt-basics/)

### Lesson 1.2: Data Quality with Expectations
- 1.2.1 Introduction
- 1.2.2 Understanding DLT expectations
- 1.2.3 Implementing expectations
- 1.2.4 Summary

**Lab:** [Lab 2 — Data Quality with Expectations](../labs/lab-2.md)
**Examples:** [`examples/dlt-basics/`](../examples/dlt-basics/), [`examples/simple-pipeline/`](../examples/simple-pipeline/)

### Lesson 1.3: Streaming with DLT
- 1.3.1 Introduction
- 1.3.2 Creating streaming tables
- 1.3.3 Working with streaming tables
- 1.3.4 Automatic schemas and challenges
- 1.3.5 Summary

**Lab:** [Lab 3 — Streaming with DLT](../labs/lab-3.md)
**Examples:** [`examples/streaming/`](../examples/streaming/)

---

## Module 2: Medallion Architecture Implementation

### Lesson 2.1: Bronze Layer Fundamentals
- 2.1.1 Introduction
- 2.1.2 Introduction to medallion architecture
- 2.1.3 Bronze layer design patterns
- 2.1.4 Ingesting data to raw delta tables
- 2.1.5 Summary

**Lab:** [Lab 4 — Bronze Layer Fundamentals](../labs/lab-4.md)
**Examples:** [`examples/simple-pipeline/bronze.py`](../examples/simple-pipeline/bronze.py)

### Lesson 2.2: Silver Layer Data Cleaning
- 2.2.1 Introduction
- 2.2.2 Exploratory analysis
- 2.2.3 Data quality and cleaning strategies
- 2.2.4 Reviewing silver layer results
- 2.2.5 Summary

**Lab:** [Lab 5 — Silver and Gold Layers](../labs/lab-5.md)
**Examples:** [`examples/simple-pipeline/`](../examples/simple-pipeline/)

### Lesson 2.3: Gold Layer Aggregation
- 2.3.1 Introduction
- 2.3.2 Applying business logic
- 2.3.3 Incremental and recompute in pipelines
- 2.3.4 Optimizations for gold tables
- 2.3.5 Summary

**Lab:** [Lab 5 — Silver and Gold Layers](../labs/lab-5.md)
**Examples:** [`examples/simple-pipeline/gold_by_region.py`](../examples/simple-pipeline/gold_by_region.py)

---

## Module 3: End-to-End Application

### Lesson 3.1: End-to-End Application
- 3.1.1 Introduction
- 3.1.2 Overview of inventory orchestration
- 3.1.3 Real-world medallion architecture
- 3.1.4 Inventory management overview
- 3.1.5 Summary

**Lab:** [Lab 6 — End-to-End Application](../labs/lab-6.md)
**Examples:** [`examples/wine-pricing-inventory/`](../examples/wine-pricing-inventory/)

### Lesson 3.2: Challenges and Next Steps
- 3.2.1 Introduction
- 3.2.2 Challenges and next steps
- 3.2.3 Course summary

**Capstone:** [Capstone Project](capstone-project.md)

---

## Quick Reference

### Learning Path

```
Module 1: DLT Fundamentals
  ├── DLT Foundations → Lab 1
  ├── Expectations    → Lab 2
  └── Streaming       → Lab 3

Module 2: Medallion Architecture
  ├── Bronze Layer    → Lab 4
  └── Silver & Gold   → Lab 5

Module 3: End-to-End
  ├── Full Pipeline   → Lab 6
  └── Capstone        → Capstone Project
```

### Prerequisites

- Basic SQL and Python knowledge
- A Databricks account (the FREE Community Edition works for all examples)
- Familiarity with data concepts (tables, schemas, ETL)

### Key Topics by Module

| Module | Topics |
|--------|--------|
| 1 | Delta Live Tables, SQL/Python pipelines, expectations, streaming, Auto Loader |
| 2 | Medallion architecture, bronze ingestion, silver cleaning, gold aggregation, Z-order |
| 3 | CDC, SCD Type 1/2, batch + streaming, production patterns, naming conventions |
