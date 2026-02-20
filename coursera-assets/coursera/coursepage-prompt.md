Generate Coursera landing page content for the following course. Output each field clearly labeled.

===== COURSE INFO =====
- Course Title: Data Engineering with Databricks (max 46 chars)
- Primary Domain: Data Engineering
- Secondary Domain: Databricks Platform
- Difficulty Level: Intermediate
- Primary Language: English
- Instructor: Noah Gift
- Partner: Coursera

===== CONFIG ENRICHMENT =====
Course Title: Data Engineering with Databricks
Project: 
Repository: github.com/alfredodeza/databricks-data-engineering

Module Titles:
  Module 1: DLT Fundamentals
  Module 2: Medallion Architecture
  Module 3: End-to-End Application

Key Concepts Vocabulary:
  Course overview and learning outcomes, Delta Live Tables as the core technology, Hands-on labs with Databricks Community Edition, What Delta Live Tables solves, Declarative vs imperative ETL, Pipeline-first approach, DLT as managed ETL framework, Materialized views vs streaming tables, Automatic dependency resolution, SQL CREATE TABLE with dlt.table decorator, Python @dlt.table and @dlt.view decorators, Reading from sources and chaining tables, Pipeline configuration in Databricks UI, Source file placement in Volumes, Running and monitoring pipeline execution, DLT provides declarative ETL, SQL and Python syntax reviewed, First pipeline created and executed, Data quality as first-class concern, Expectations enforce constraints at pipeline level, Three enforcement modes, EXPECT: warn on violation, keep rows, EXPECT OR DROP: silently remove bad rows, EXPECT OR FAIL: halt pipeline on violation, Adding expectations to SQL and Python pipelines, Multiple expectations per table, Monitoring expectation violations in UI, Three enforcement modes reviewed, Expectations integrated into pipeline code, Quality metrics captured automatically, Batch vs streaming ingestion, Auto Loader for incremental file processing, Streaming tables in DLT, Auto Loader with cloudFiles format, Schema inference and evolution, Streaming table vs materialized view, Append-only vs complete recompute, Chaining streaming tables together, Triggered vs continuous execution modes, Schema inference with rescue column, Schema evolution and merging strategies, Common streaming pitfalls and solutions, Auto Loader and streaming tables reviewed, Schema evolution strategies covered, Batch vs streaming tradeoffs understood, Medallion architecture overview, Bronze as the raw ingestion layer, Immutability and audit trail, Three-layer data organization pattern, Bronze: raw, Silver: cleaned, Gold: business, Each layer adds quality and structure, Landing zone to bronze table patterns, File format handling (CSV, JSON, Parquet), Metadata columns for lineage tracking, Creating bronze tables from Volumes, Delta Lake format for ACID guarantees, Incremental ingestion with Auto Loader, Medallion architecture pattern established, Bronze layer ingestion patterns reviewed, Delta Lake as the storage foundation, Silver as the cleaned and conformed layer, Data quality and normalization, Bridging raw data to business logic, Profiling bronze data for quality issues, Identifying nulls, duplicates, and outliers, Establishing cleaning rules from exploration, Type casting and null handling, Deduplication strategies, Expectations as quality gates between layers, Querying silver tables for quality checks, Comparing bronze vs silver row counts, Validating expectation violation metrics, Exploratory analysis informs cleaning, Silver layer applies type safety and dedup, Expectations bridge bronze to silver, Gold as the business logic layer, Aggregations, joins, and derived metrics, Serving analytics and ML consumers, Aggregation patterns (GROUP BY, window functions), Joining silver tables for enrichment, Naming conventions for gold tables, Full recompute vs incremental append, Cost and latency tradeoffs, Z-ordering for query performance, Partitioning strategies, Table properties and auto-optimization, Gold tables serve business consumers, Incremental vs recompute reviewed, Z-ordering and partitioning for performance, Building a complete production pipeline, Combining DLT, expectations, and medallion layers, Change Data Capture with apply_changes(), Wine pricing inventory system design, Multi-source ingestion pattern, Orchestrating dependent tables, SCD Type 1 vs Type 2 patterns, apply_changes() for CDC processing, Handling late-arriving and out-of-order data, End-to-end pipeline execution, Monitoring pipeline health and metrics, Debugging expectation failures, Complete pipeline with CDC implemented, Medallion architecture in production context, Lab 6 builds the inventory system, Common data engineering challenges, Scaling pipelines beyond single pipelines, Career growth in data engineering, Multi-pipeline orchestration with Workflows, Unity Catalog for governance, Real-time streaming beyond batch, DLT foundations and syntax, Expectations for data quality, Medallion architecture: bronze, silver, gold

===== COURSE STRUCTURE =====
Duration: 3 weeks

Week 1: DLT Fundamentals
  Learning Objectives:
  - Remember core terminology and foundational concepts
  - Understand the relationships between key system components
  - Apply basic techniques to introductory problems
  Lessons:
  - 1.1: Course Introduction (6 videos)
  - 1.2: Expectations (4 videos)
  - 1.3: Streaming (5 videos)

Week 2: Medallion Architecture
  Learning Objectives:
  - Analyze system architectures and identify design patterns
  - Apply intermediate techniques to solve practical problems
  - Evaluate trade-offs between competing approaches
  Lessons:
  - 2.1: Bronze Layer (5 videos)
  - 2.2: Silver Layer (5 videos)
  - 2.3: Gold Layer (5 videos)

Week 3: Capstone Project
  Learning Objectives:
  - Create an end-to-end solution integrating all course concepts
  - Evaluate the solution against production quality standards
  - Synthesize learnings from previous modules into a cohesive project
  Lessons:
  - 3.1: End-to-End Application (5 videos)
  - 3.2: Challenges (3 videos)

===== TRANSCRIPT EXCERPTS =====
Week 1:
Let's start working with Delta Live Tables. But before we work with Delta Live Tables, let's have a brief overview of what they are and how they can help us out. At the end of the day, we want to know how we can interact with our data and DLT Delta Live tables is going to definitely help us. There's plenty to cover with Databricks and Data Engineering. From the Medali-Narchitecture, we'll find out what is exactly the Medaline architecture and what are the components all the way through...

Week 2:
[MUSIC] Let's ingest raw data to create a delta table. Now, how do we do this? Well, there's a couple of different ways you can do this in specifically concentrating into the bronze architecture for having data into the brown state. So one of the ways that we can do this here in the Databricks dashboard is we're going to go to the Data Engineering portion and The menu for data ingestion now when you're here, you can actually use some of The connectors in this case Amazon S3 is definitely an...

Week 3:
[MUSIC] Let's do an overview of our inventory orchestration or pipelines, our data, how everything works in the Databricks platform. This inventory volume will allow us to get the data that we want. Now, as you know with Databricks, you have different many different options. Data can be ingested from many different places. You could even challenge this architecture of not having raw files defined in here within Databrics but they storage solution from Amazon. It doesn't matter where it is, but...

===== SKILL VOCABULARY =====
Analysis, And, Applying, Architecture, Automatic, Bronze, Business, Challenges, Cleaning, Course

===== GENERATE THE FOLLOWING =====
1. COURSE NAME (<=46 chars, permanent — make it count)
2. COURSE DESCRIPTION (150-200 words / 800-1200 chars)
   - Open with learning outcomes
   - Explain learner benefit
   - State what makes it unique
   - No fluff — every sentence earns its place
3. ESTIMATED WORKLOAD (<=100 chars, format: "X weeks of study, Y-Z hours/week")
4. RECOMMENDED BACKGROUND (<=150 chars)
5. SKILL TAGS (5-10 keywords for discoverability)
6. WHAT YOU WILL LEARN (2-3 bullet points, concise)
7. FAQs (2-3 Q&A pairs addressing common objections)
8. IMAGE GUIDANCE (describe ideal subjects for):
   - Logo Image (800x800-1200x1200 square)
   - Marketing Image (1200x600, 2:1 ratio)
