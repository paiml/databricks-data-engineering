# databricks-data-engineering

Hands-on course for building data pipelines with Databricks Delta Live Tables and the medallion architecture. Part of
the **Enterprise AI and Data Engineering with Databricks** specialization on Coursera.

## Language

- **Primary:** Python (Databricks notebooks) and SQL (DLT pipelines)
- **Config:** Lua course config in `resolve-pipeline/config/databricks_de.lua`
- **Labs:** Markdown with Databricks notebook instructions

## Structure

```
examples/
  dlt-basics/              -- SQL-based DLT pipeline
  streaming/               -- Batch vs streaming with Auto Loader
  simple-pipeline/         -- Wine ratings Bronze-Silver-Gold
  wine-pricing-inventory/  -- End-to-end pipeline with CDC
labs/                      -- Hands-on lab instructions (6 labs)
docs/                      -- Course outline and capstone project
coursera-assets/
  output/                  -- Rendered course videos (rmedia output)
```

## Course Structure

- **Module 1: DLT Fundamentals** — Pipeline creation, expectations, streaming (3 lessons, 15 videos)
- **Module 2: Medallion Architecture** — Bronze/silver/gold layers (3 lessons, 15 videos)
- **Module 3: End-to-End Application** — Capstone pipeline with CDC (2 lessons, 8 videos)

## Coursera Marketing Assets

Marketing assets are generated from `resolve-pipeline` using 8 Claude Code slash commands. The config file is
`resolve-pipeline/config/databricks_de.lua` and the source directory is `coursera-assets/output/`.

Generated assets go to `/tmp/coursera-out/` by default. See the resolve-pipeline README for the full command reference.

## Commands

```bash
# No local build — all examples run in Databricks workspace
# Upload examples/ to Databricks, create DLT pipelines, run them
```
