# Role Play: Medallion Architecture

## Scenario

**Your Role**: Data Engineer at FreshMart, a regional retail chain with 120 stores across the southeastern United States.

**Context**: FreshMart is undergoing a digital transformation. The company has point-of-sale (POS) systems in every store generating transaction records, a loyalty program with 2 million active members, a supply chain system tracking inventory shipments from 15 distribution centers, and a recently launched e-commerce platform. Each system exports data in a different format -- the POS systems produce fixed-width flat files every 15 minutes, the loyalty system writes to a PostgreSQL database that is replicated via Change Data Capture (CDC), the supply chain system emits JavaScript Object Notation (JSON) events to a Kafka topic, and the e-commerce platform logs events to cloud storage as Parquet files.

The Vice President (VP) of Analytics has commissioned a new retail analytics platform on Databricks. The platform must unify data from all four sources into a consistent data model that supports three primary use cases: real-time store performance dashboards (updated within 30 minutes), weekly customer segmentation reports for the marketing team, and monthly supply chain optimization analysis. The current state is chaos -- each analyst has their own set of notebooks that read from raw files, apply ad-hoc cleaning logic, and produce one-off tables that no one else can reproduce.

Your manager has asked you to design the medallion architecture for this platform. You need to define what lives in each layer, how data flows from raw sources to business-ready tables, and how you will ensure data quality and consistency across all four sources. The design must support the three use cases with their different freshness requirements while minimizing compute costs. FreshMart's data team has three engineers (including you) and cannot afford to maintain dozens of bespoke pipelines.

## Tasks

### Task 1: Design the Bronze Layer

For each of the four data sources, define how raw data will be ingested into the bronze layer. Specify the ingestion method (Auto Loader, COPY INTO, streaming), the file format handling, and how you will preserve the raw data for auditability. Address the challenge of four different source formats landing in a unified lakehouse architecture. Explain your partitioning and clustering strategy for each bronze table.

### Task 2: Design the Silver and Gold Layers

Define the silver layer tables that conform and cleanse the four sources into a consistent data model. Specify the join keys that connect transactions to customers to inventory. Then define the gold layer tables that serve each of the three use cases -- store dashboards, customer segmentation, and supply chain optimization. For each gold table, explain what aggregation or transformation produces it from silver, and how its refresh cadence meets the business freshness requirement.

### Task 3: Evaluate Trade-offs and Present Recommendations

Assess the cost-performance trade-offs of your design. Where did you choose streaming versus batch and why? How would you handle late-arriving data from the POS systems (a store's network goes offline for 2 hours, then uploads a backlog)? What expectations would you define at the silver layer to catch integration issues like orphaned transactions (a transaction references a `customer_id` that does not exist in the loyalty system)? Present your architecture as a diagram description and a table of pipeline configurations.

## AI Persona

**Title**: VP of Analytics

**Overview**: A business-oriented analytics leader with a technical background in Structured Query Language (SQL) and data warehousing. They care deeply about data trust and reproducibility after years of dealing with inconsistent analyst-built pipelines. They will push for clarity on how the architecture prevents the current chaos of ad-hoc notebooks and will ask pointed questions about operational cost and team capacity constraints.

## Evaluation Criteria

### Advanced

- Each data source is handled with an ingestion pattern that accounts for its format, delivery cadence, and reliability characteristics
- Silver layer enforces a consistent data model with clear grain definitions and explicit handling of referential integrity gaps across sources
- Gold layer is purpose-built for each use case with refresh cadences matching business requirements without over-processing
- Design is operationally feasible for a three-person team with realistic maintenance burden estimates

### Intermediate

- Correctly identifies appropriate ingestion methods for each source format and preserves raw data in bronze without premature transformation
- Silver layer applies reasonable cleaning and deduplication with some expectations defined
- Gold layer tables serve the three use cases but may not fully optimize refresh cadences or cost
- Architecture is generally sound but may have gaps in late-arriving data handling or cross-source joins

### Beginner

- Demonstrates understanding of the medallion architecture layers and can assign data sources to bronze tables
- Attempts silver layer design but may conflate cleaning with business logic or miss cross-source integration challenges
- Gold layer exists but may be overly generic rather than purpose-built for specific use cases
- Recognizes operational constraints but does not fully address how the design fits within team capacity
