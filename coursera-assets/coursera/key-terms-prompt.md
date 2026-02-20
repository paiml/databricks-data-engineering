Generate key-terms markdown AND a banner SVG for a course lesson.
Follow the instructions precisely. Output both artifacts.

===== COURSE CONTEXT =====
Course: Data Engineering with Databricks
Structure: 3 modules, 3 lessons/module

Module 1: DLT Fundamentals
  Lesson 1.1: Course Introduction
  Lesson 1.2: Expectations
  Lesson 1.3: Streaming
Module 2: Medallion Architecture
  Lesson 2.1: Bronze Layer
  Lesson 2.2: Silver Layer
  Lesson 2.3: Gold Layer
Module 3: Capstone Project
  Lesson 3.1: End-to-End Application
  Lesson 3.2: Challenges

===== CONFIG KEY CONCEPTS =====
Lesson 1.1 (Course Introduction):
  - Course overview and learning outcomes
  - Delta Live Tables as the core technology
  - Hands-on labs with Databricks Community Edition
Lesson 1.1 (DLT Foundations Introduction):
  - What Delta Live Tables solves
  - Declarative vs imperative ETL
  - Pipeline-first approach
Lesson 1.1 (Introduction to Delta Live Tables):
  - DLT as managed ETL framework
  - Materialized views vs streaming tables
  - Automatic dependency resolution
Lesson 1.1 (DLT Syntax with Python and SQL):
  - SQL CREATE TABLE with dlt.table decorator
  - Python @dlt.table and @dlt.view decorators
  - Reading from sources and chaining tables
Lesson 1.1 (Creating Your First DLT Pipeline):
  - Pipeline configuration in Databricks UI
  - Source file placement in Volumes
  - Running and monitoring pipeline execution
Lesson 1.1 (DLT Foundations Summary):
  - DLT provides declarative ETL
  - SQL and Python syntax reviewed
  - First pipeline created and executed
Lesson 1.2 (Expectations Introduction):
  - Data quality as first-class concern
  - Expectations enforce constraints at pipeline level
  - Three enforcement modes
Lesson 1.2 (Understanding DLT Expectations):
  - EXPECT: warn on violation, keep rows
  - EXPECT OR DROP: silently remove bad rows
  - EXPECT OR FAIL: halt pipeline on violation
Lesson 1.2 (Implementing Expectations):
  - Adding expectations to SQL and Python pipelines
  - Multiple expectations per table
  - Monitoring expectation violations in UI
Lesson 1.2 (Expectations Summary):
  - Three enforcement modes reviewed
  - Expectations integrated into pipeline code
  - Quality metrics captured automatically
Lesson 1.3 (Streaming Introduction):
  - Batch vs streaming ingestion
  - Auto Loader for incremental file processing
  - Streaming tables in DLT
Lesson 1.3 (Creating Streaming Tables):
  - Auto Loader with cloudFiles format
  - Schema inference and evolution
  - Streaming table vs materialized view
Lesson 1.3 (Working with Streaming Tables):
  - Append-only vs complete recompute
  - Chaining streaming tables together
  - Triggered vs continuous execution modes
Lesson 1.3 (Automatic Schemas and Challenges):
  - Schema inference with rescue column
  - Schema evolution and merging strategies
  - Common streaming pitfalls and solutions
Lesson 1.3 (Streaming Summary):
  - Auto Loader and streaming tables reviewed
  - Schema evolution strategies covered
  - Batch vs streaming tradeoffs understood
Lesson 2.1 (Bronze Layer Introduction):
  - Medallion architecture overview
  - Bronze as the raw ingestion layer
  - Immutability and audit trail
Lesson 2.1 (Introduction to Medallion Architecture):
  - Three-layer data organization pattern
  - Bronze: raw, Silver: cleaned, Gold: business
  - Each layer adds quality and structure
Lesson 2.1 (Bronze Layer Design Patterns):
  - Landing zone to bronze table patterns
  - File format handling (CSV, JSON, Parquet)
  - Metadata columns for lineage tracking
Lesson 2.1 (Ingesting Data to Raw Delta Tables):
  - Creating bronze tables from Volumes
  - Delta Lake format for ACID guarantees
  - Incremental ingestion with Auto Loader
Lesson 2.1 (Bronze Layer Summary):
  - Medallion architecture pattern established
  - Bronze layer ingestion patterns reviewed
  - Delta Lake as the storage foundation
Lesson 2.2 (Silver Layer Introduction):
  - Silver as the cleaned and conformed layer
  - Data quality and normalization
  - Bridging raw data to business logic
Lesson 2.2 (Exploratory Analysis):
  - Profiling bronze data for quality issues
  - Identifying nulls, duplicates, and outliers
  - Establishing cleaning rules from exploration
Lesson 2.2 (Data Quality and Cleaning Strategies):
  - Type casting and null handling
  - Deduplication strategies
  - Expectations as quality gates between layers
Lesson 2.2 (Reviewing Silver Layer Results):
  - Querying silver tables for quality checks
  - Comparing bronze vs silver row counts
  - Validating expectation violation metrics
Lesson 2.2 (Silver Layer Summary):
  - Exploratory analysis informs cleaning
  - Silver layer applies type safety and dedup
  - Expectations bridge bronze to silver
Lesson 2.3 (Gold Layer Introduction):
  - Gold as the business logic layer
  - Aggregations, joins, and derived metrics
  - Serving analytics and ML consumers
Lesson 2.3 (Applying Business Logic):
  - Aggregation patterns (GROUP BY, window functions)
  - Joining silver tables for enrichment
  - Naming conventions for gold tables
Lesson 2.3 (Incremental and Recompute in Pipelines):
  - Full recompute vs incremental append
  - Materialized views vs streaming tables
  - Cost and latency tradeoffs
Lesson 2.3 (Optimizations for Gold Tables):
  - Z-ordering for query performance
  - Partitioning strategies
  - Table properties and auto-optimization
Lesson 2.3 (Gold Layer Summary):
  - Gold tables serve business consumers
  - Incremental vs recompute reviewed
  - Z-ordering and partitioning for performance
Lesson 3.1 (End-to-End Application Introduction):
  - Building a complete production pipeline
  - Combining DLT, expectations, and medallion layers
  - Change Data Capture with apply_changes()
Lesson 3.1 (Overview of Inventory Orchestration):
  - Wine pricing inventory system design
  - Multi-source ingestion pattern
  - Orchestrating dependent tables
Lesson 3.1 (Real-World Medallion Architecture):
  - SCD Type 1 vs Type 2 patterns
  - apply_changes() for CDC processing
  - Handling late-arriving and out-of-order data
Lesson 3.1 (Inventory Management Overview):
  - End-to-end pipeline execution
  - Monitoring pipeline health and metrics
  - Debugging expectation failures
Lesson 3.1 (End-to-End Application Summary):
  - Complete pipeline with CDC implemented
  - Medallion architecture in production context
  - Lab 6 builds the inventory system
Lesson 3.2 (Challenges Introduction):
  - Common data engineering challenges
  - Scaling pipelines beyond single pipelines
  - Career growth in data engineering
Lesson 3.2 (Challenges and Next Steps):
  - Multi-pipeline orchestration with Workflows
  - Unity Catalog for governance
  - Real-time streaming beyond batch
Lesson 3.2 (Course Summary):
  - DLT foundations and syntax
  - Expectations for data quality
  - Medallion architecture: bronze, silver, gold

===== TRANSCRIPT EXCERPTS =====
Module 1:
Let's start working with Delta Live Tables. But before we work with Delta Live Tables, let's have a brief overview of what they are and how they can help us out. At the end of the day, we want to know how we can interact with our data and DLT Delta Live tables is going to definitely help us. There's plenty to cover with Databricks and Data Engineering. From the Medali-Narchitecture, we'll find out what is exactly the Medaline architecture and what are the components all the way through...

Module 2:
[MUSIC] Let's ingest raw data to create a delta table. Now, how do we do this? Well, there's a couple of different ways you can do this in specifically concentrating into the bronze architecture for having data into the brown state. So one of the ways that we can do this here in the Databricks dashboard is we're going to go to the Data Engineering portion and The menu for data ingestion now when you're here, you can actually use some of The connectors in this case Amazon S3 is definitely an...

Module 3:
[MUSIC] Let's do an overview of our inventory orchestration or pipelines, our data, how everything works in the Databricks platform. This inventory volume will allow us to get the data that we want. Now, as you know with Databricks, you have different many different options. Data can be ingested from many different places. You could even challenge this architecture of not having raw files defined in here within Databrics but they storage solution from Amazon. It doesn't matter where it is, but...


===== SVG GRID PROTOCOL (v2, condensed) =====

CANVAS: 1920x1080, viewBox="0 0 1920 1080", xmlns="http://www.w3.org/2000/svg"
GRID: 16 columns x 9 rows, cell = 120px x 120px
COORD FORMULA: x = col * 120, y = row * 120 (0-indexed)
INTERNAL PADDING: 20px inside every block (text starts at x+20, y+20)
BLOCK GAP: minimum 10px between adjacent blocks

TYPOGRAPHY (hard minimums):
  - Titles: 48-64px, font-weight 700
  - Headings: 36-48px, font-weight 700
  - Body: 24-32px, font-weight 400
  - Labels: 18-24px, font-weight 600
  - HARD FLOOR: 18px minimum for ANY text element
  - font-family: "Source Sans 3", "Inter", sans-serif

TEXT WIDTH BUDGET (approximate char widths at common sizes):
  Size  | Avg char width | Max chars in 1920px (with 120px margins)
  64px  | 35px          | 48
  48px  | 26px          | 64
  36px  | 20px          | 84
  24px  | 13px          | 129

COLOR PALETTE (dark theme, WCAG AA):
  Background:  #0f1114 (near-black)
  Foreground:  #ffffff (white, primary text)
  Accent:      #4a9eff (blue, headings/dividers)
  Muted:       #ffffff at 65% opacity (descriptions)
  Card BG:     #1a1d23 (elevated surfaces)
  Card Border: #2a2d33 (subtle edge)

PAINT ORDER: background rect first, then decorative elements, then text on top.

DESIGN RULES:
  1. Every text element must have a fill color from the palette
  2. All text must be inside the 120px margin on each side (x: 120..1800)
  3. No text may overlap another text element
  4. Rounded rectangles use rx="12" for cards, rx="20" for pills
  5. Divider lines: height="4" or height="6", accent color
  6. No external images, links, or scripts
  7. No text below y=1020 (60px bottom margin)
  8. Group related elements in <g> tags with descriptive id attributes

VALIDATION CHECKLIST:
  [ ] viewBox="0 0 1920 1080"
  [ ] All text >= 18px font-size
  [ ] All text within x: 120..1800
  [ ] No text below y=1020
  [ ] Background rect covers full canvas
  [ ] All colors from palette
  [ ] No overlapping text elements
  [ ] All blocks have internal 20px padding
  [ ] 10px minimum gap between blocks
  [ ] XML comment with GRID PROTOCOL MANIFEST at end of SVG

MANIFEST FORMAT (XML comment before closing </svg>):
  <!-- GRID PROTOCOL MANIFEST
  template: [Template Name]
  grid_cells_used: [list of col,row pairs]
  font_sizes: [list of sizes used]
  min_font_size: [smallest size]
  text_elements: [count]
  palette_colors: [list of hex colors used]
  -->

===== TEMPLATE F: KEY CONCEPTS BANNER =====

LAYOUT: 4 concept cards arranged horizontally across the canvas.
STRUCTURE:
  - Title bar: rows 0-1, full width, accent background
    "Key Terms" heading centered, 56px white bold
  - 4 cards: rows 2-8, each card spans 3.5 columns with 0.5 col gap
    Card 1: cols 0.5-4,   Card 2: cols 4.5-8
    Card 3: cols 8.5-12,  Card 4: cols 13-16 (approximate)
  - Each card:
    - Background: #1a1d23 rounded rect (rx=12)
    - Term name: 32px accent bold, top of card (y = card_top + 40)
    - Definition: 22px white 65% opacity, below term (y = term_y + 50)
    - Definition wraps at card width minus 40px padding

CARD POSITIONS (pixel coordinates):
  Card 1: x=60,  y=260, w=420, h=680
  Card 2: x=510, y=260, w=420, h=680
  Card 3: x=960, y=260, w=420, h=680
  Card 4: x=1410, y=260, w=420, h=680

RULES:
  - Select exactly 4 of the 5 key terms (pick the 4 most visual)
  - Term name max ~18 chars (truncate with ellipsis if needed)
  - Definition max ~80 chars (2-3 short lines at 22px)
  - Accent-colored left border (4px wide) on each card for visual rhythm

===== OUTPUT 1: key-terms.md =====
Generate exactly 5 key technical terms extracted from the transcript.
Format:

# Key Terms

## {Term 1}
{Definition — 1-2 sentences, factual, no "the speaker says..."}

## {Term 2}
{Definition}

## {Term 3}
{Definition}

## {Term 4}
{Definition}

## {Term 5}
{Definition}

## References

- [Author et al., "Paper Title," arXiv:NNNN.NNNNN, YYYY](https://arxiv.org/abs/NNNN.NNNNN)
- [Author et al., "Paper Title," arXiv:NNNN.NNNNN, YYYY](https://arxiv.org/abs/NNNN.NNNNN)

RULES:
- Terms must appear in or be directly supported by the transcript
- Definitions are concise, factual, and standalone
- No first-person or speaker attribution
- Terms sorted by order of appearance in transcript
- Include a ## References section at the end with 2-3 arXiv paper links
- Each reference MUST be a real, verifiable arXiv paper — URLs will be checked via HTTP
- References must be directly relevant to the key terms defined above
- Expand all acronyms on first use: "Graphics Processing Unit (GPU)"
- Use correct proper-noun spelling — names will be validated against the course dictionary
- NEVER include TODO, TBD, FIXME, or placeholder text

===== OUTPUT 2: key-terms-banner.svg =====
Follow the SVG Grid Protocol above to create a 1920x1080 banner.
Use Template F (Key Concepts Banner): 4 concept cards horizontal layout.
Select the 4 most visually distinct terms from your 5 key terms.
Include the GRID PROTOCOL MANIFEST as an XML comment before </svg>.
