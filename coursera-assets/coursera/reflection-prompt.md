Generate reflection markdown AND a banner SVG for a course lesson.
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

===== CONFIG REFLECTION PROMPTS =====
Lesson 1.1 (Course Introduction):
  - Pipelines are the backbone of data engineering
  - Free Databricks CE is sufficient for all labs
Lesson 1.1 (DLT Foundations Introduction):
  - DLT abstracts away orchestration complexity
  - Focus on what, not how
Lesson 1.1 (Introduction to Delta Live Tables):
  - DLT manages lifecycle and dependencies
  - SQL and Python both supported
Lesson 1.1 (DLT Syntax with Python and SQL):
  - Same pipeline, two language options
  - Decorator pattern simplifies table definitions
Lesson 1.1 (Creating Your First DLT Pipeline):
  - Pipelines are configured, not coded
  - Event log provides full execution lineage
Lesson 1.1 (DLT Foundations Summary):
  - Foundation set for expectations and streaming
  - Lab 1 reinforces DLT basics
Lesson 1.2 (Expectations Introduction):
  - Quality gates prevent bad data propagation
  - Shift validation left into the pipeline
Lesson 1.2 (Understanding DLT Expectations):
  - Choose enforcement mode based on data criticality
  - Metrics track violation counts automatically
Lesson 1.2 (Implementing Expectations):
  - Expectations are declarative quality contracts
  - Combine multiple constraints for defense in depth
Lesson 1.2 (Expectations Summary):
  - Data quality is not optional in production
  - Lab 2 practices expectation patterns
Lesson 1.3 (Streaming Introduction):
  - Streaming enables near-real-time pipelines
  - Auto Loader eliminates manual file tracking
Lesson 1.3 (Creating Streaming Tables):
  - Auto Loader handles new files automatically
  - Schema evolution prevents pipeline breaks
Lesson 1.3 (Working with Streaming Tables):
  - Streaming tables are append-only by default
  - Pipeline mode determines processing frequency
Lesson 1.3 (Automatic Schemas and Challenges):
  - Rescue column catches schema drift
  - Plan for schema changes in production
Lesson 1.3 (Streaming Summary):
  - Streaming completes the DLT toolkit
  - Lab 3 practices streaming patterns
Lesson 2.1 (Bronze Layer Introduction):
  - Bronze preserves raw data for reprocessing
  - Never transform at the bronze layer
Lesson 2.1 (Introduction to Medallion Architecture):
  - Medallion architecture is a data contract
  - Layers decouple ingestion from consumption
Lesson 2.1 (Bronze Layer Design Patterns):
  - Metadata enrichment enables debugging
  - Format-agnostic ingestion with Auto Loader
Lesson 2.1 (Ingesting Data to Raw Delta Tables):
  - Delta Lake provides time travel and versioning
  - Bronze tables grow append-only
Lesson 2.1 (Bronze Layer Summary):
  - Bronze is the single source of truth
  - Lab 4 builds a bronze pipeline
Lesson 2.2 (Silver Layer Introduction):
  - Silver is where data becomes trustworthy
  - Cleaning strategies depend on domain
Lesson 2.2 (Exploratory Analysis):
  - Explore before you transform
  - Data profiling informs expectation design
Lesson 2.2 (Data Quality and Cleaning Strategies):
  - Silver tables enforce a schema contract
  - Expectations catch regressions automatically
Lesson 2.2 (Reviewing Silver Layer Results):
  - Validate outputs, not just inputs
  - Row count deltas reveal cleaning impact
Lesson 2.2 (Silver Layer Summary):
  - Silver is the reliability layer
  - Lab 5 practices silver and gold patterns
Lesson 2.3 (Gold Layer Introduction):
  - Gold tables are consumption-ready
  - Design gold tables for specific use cases
Lesson 2.3 (Applying Business Logic):
  - Gold tables encode business decisions
  - One gold table per business question
Lesson 2.3 (Incremental and Recompute in Pipelines):
  - Incremental saves compute, full ensures correctness
  - Choose strategy per table, not per pipeline
Lesson 2.3 (Optimizations for Gold Tables):
  - Z-order on high-cardinality filter columns
  - Partitioning helps when queries are selective
Lesson 2.3 (Gold Layer Summary):
  - Complete medallion architecture implemented
  - Lab 5 covers silver and gold together
Lesson 3.1 (End-to-End Application Introduction):
  - Production pipelines combine all prior concepts
  - CDC handles real-world data mutations
Lesson 3.1 (Overview of Inventory Orchestration):
  - Real systems have multiple data sources
  - DLT resolves dependencies automatically
Lesson 3.1 (Real-World Medallion Architecture):
  - SCD Type 2 preserves historical state
  - apply_changes() simplifies CDC logic
Lesson 3.1 (Inventory Management Overview):
  - Observability is essential in production
  - Expectation metrics surface issues early
Lesson 3.1 (End-to-End Application Summary):
  - All concepts integrated into one pipeline
  - Capstone project extends this pattern
Lesson 3.2 (Challenges Introduction):
  - Challenges drive engineering growth
  - Data engineering is an evolving discipline
Lesson 3.2 (Challenges and Next Steps):
  - Governance and orchestration are next frontiers
  - Unity Catalog unifies data and AI assets
Lesson 3.2 (Course Summary):
  - Production pipelines need all three layers
  - Capstone project demonstrates mastery

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

===== TEMPLATE G: REFLECTION BANNER =====

LAYOUT: Visual-only banner with abstract geometric motifs.
PURPOSE: Decorative banner for lesson reflection sections.

STRUCTURE:
  - Full canvas background: #0f1114
  - Gradient overlay from top (transparent) to bottom (#0f1114 at 40%)
  - Central motif: abstract geometric shapes suggesting contemplation
    - Large circle or hexagon, accent color at 15% opacity (centered)
    - 3-4 smaller geometric elements arranged around center
    - Thin accent lines connecting shapes (stroke-width: 2)
  - Title: "Reflection" in 56px accent bold, centered at y=200
  - Accent divider: centered below title, 400px wide, 4px height
  - Maximum 4 single-word labels (24px, muted) near geometric shapes
    (e.g., "Connect", "Apply", "Evaluate", "Synthesize")

RULES:
  - NO paragraphs, NO multi-word text blocks, NO URLs
  - Only single-word labels (max 4 total)
  - Geometric shapes use accent color at low opacity (10-25%)
  - Keep visual weight centered (don't cluster shapes on one side)
  - All shapes must be SVG primitives (circle, rect, polygon, line)
  - No external images or embedded bitmaps

===== OUTPUT 1: reflection.md =====
Generate a structured reflection document based on the transcript content.
Format:

# Reflection

## Key Points

1. **{Point 1}**: {Application to real-world scenario}
2. **{Point 2}**: {Application to real-world scenario}
3. **{Point 3}**: {Application to real-world scenario}

## Practical Scenarios

### Scenario 1: {Title}

**Situation**: {Description of a real-world situation}

**Solution**: {How to apply the lesson concepts}

### Scenario 2: {Title}

**Situation**: {Description of a real-world situation}

**Solution**: {How to apply the lesson concepts}

## Journal Prompt

{Open-ended question for self-reflection that connects lesson content to the learner's experience}

## References

- [Author et al., "Paper Title," arXiv:NNNN.NNNNN, YYYY](https://arxiv.org/abs/NNNN.NNNNN)
- [Author et al., "Paper Title," arXiv:NNNN.NNNNN, YYYY](https://arxiv.org/abs/NNNN.NNNNN)

RULES:
- Key points must connect directly to transcript content
- Scenarios should be realistic and actionable
- No first-person or speaker attribution
- Journal prompt should encourage critical thinking
- Include a ## References section at the end with 2-3 arXiv paper links
- Each reference MUST be a real, verifiable arXiv paper — URLs will be checked via HTTP
- References must be directly relevant to the reflection scenarios above
- Expand all acronyms on first use: "Graphics Processing Unit (GPU)"
- Use correct proper-noun spelling — names will be validated against the course dictionary
- NEVER include TODO, TBD, FIXME, or placeholder text

===== OUTPUT 2: reflection-banner.svg =====
Follow the SVG Grid Protocol above to create a 1920x1080 banner.
Use Template G (Reflection Banner): visual-only with abstract geometric motifs.
Maximum 4 single-word labels. No paragraphs, no URLs.
Include the GRID PROTOCOL MANIFEST as an XML comment before </svg>.
