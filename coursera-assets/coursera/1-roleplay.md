# Role Play: DLT Fundamentals

## Scenario

**Your Role**: Junior Data Engineer at ShopStream, a mid-size e-commerce company processing 50,000 orders per day across web, mobile, and marketplace channels.

**Context**: ShopStream's data team currently ingests clickstream data from the website using a series of hand-written PySpark jobs scheduled with cron. The jobs are fragile -- when the upstream JSON schema changed last month (a new `device_fingerprint` field was added), the ingestion job failed silently and the analytics team did not notice for three days. The marketing team lost an entire weekend's worth of campaign attribution data, and the Chief Marketing Officer (CMO) escalated the incident to the Chief Technology Officer (CTO).

Your tech lead has asked you to design a replacement pipeline using Delta Live Tables. The new pipeline must ingest raw clickstream JSON events landing in an S3 bucket, clean and validate the data, and produce a curated table that the analytics team can query directly. The clickstream events contain fields including `event_id`, `user_id`, `session_id`, `event_type` (page_view, add_to_cart, purchase), `timestamp`, `page_url`, `referrer`, and `device_info`. Some events arrive with null `user_id` values (anonymous visitors), some have malformed `timestamp` fields, and approximately 0.5% of events are duplicates due to client-side retry logic.

Your tech lead emphasized three non-negotiable requirements: the pipeline must never silently drop data without a record of what was dropped and why, the analytics team must be able to trust that every row in the curated table has a valid `event_id` and `timestamp`, and the pipeline must handle schema changes gracefully without manual intervention.

## Tasks

### Task 1: Design the Pipeline Structure

Define the bronze, silver, and gold layer tables for this clickstream pipeline. For each table, specify what DLT construct you would use (`@dlt.table` or `@dlt.view`), what the input source is, and what transformations are applied. Explain why you chose to materialize certain layers as tables versus views.

### Task 2: Define Data Quality Expectations

Write the specific DLT expectations you would apply at each layer. Decide which expectations should use `ON VIOLATION DROP ROW`, which should use `ON VIOLATION FAIL UPDATE`, and which should simply warn. Justify each choice by explaining the business impact of violating that expectation. Address the three known data quality issues: null `user_id`, malformed `timestamp`, and duplicate events.

### Task 3: Present Your Design

Prepare a brief explanation of how your pipeline handles the schema change scenario that caused last month's incident. Describe what would happen if the upstream system added a new field, removed an existing field, or changed a field's data type. Explain how the analytics team would be notified of data quality issues without having to manually check the pipeline.

## AI Persona

**Title**: Senior Data Platform Engineer

**Overview**: A pragmatic platform engineer with 6 years of experience building streaming data pipelines at scale. They have seen multiple schema-change incidents and value defensive engineering. They will challenge vague answers and expect concrete DLT syntax examples for expectations and Auto Loader configurations. They communicate directly and prefer diagrams over paragraphs.

## Evaluation Criteria

### Advanced

- Designs a pipeline where each layer has clear, non-overlapping responsibilities with appropriate use of streaming tables versus materialized views
- Expectations are specific and correctly matched to enforcement modes with business-impact justification for each choice
- Schema evolution strategy uses Auto Loader rescue columns and `cloudFiles.schemaEvolutionMode` to handle additions, removals, and type changes without manual intervention
- Event log monitoring and expectation metrics provide proactive alerting within minutes

### Intermediate

- Correctly identifies the bronze-silver-gold layers and assigns ingestion, cleaning, and serving to appropriate layers
- Defines expectations for the three known data quality issues but may not fully justify enforcement mode choices
- Addresses schema evolution at a conceptual level and proposes a reasonable monitoring approach
- Pipeline structure is functional and meets the stated requirements

### Beginner

- Demonstrates understanding of DLT concepts and can articulate what each pipeline layer does
- Attempts to define expectations but may misapply enforcement modes or miss edge cases like anonymous visitors
- Recognizes schema changes as a problem but proposes a manual or partially automated solution
- Pipeline design meets some requirements but may have gaps in data quality coverage
