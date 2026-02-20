# Role Play: Capstone Project

## Scenario

**Your Role**: Senior Data Engineer at MedSupply Corp, a medical device distributor serving 3,000 hospitals across North America. You are leading a pipeline migration project from a legacy on-premises Extract, Transform, Load (ETL) system to Databricks.

**Context**: MedSupply Corp distributes over 40,000 Stock Keeping Units (SKUs) of medical devices, from surgical instruments to diagnostic equipment. The company's legacy inventory management system runs on an Oracle database with a nightly batch ETL process built in Informatica. This system tracks purchase orders from hospitals, shipments from manufacturers, warehouse stock levels across 8 distribution centers, and product recalls. The nightly batch process has become the single biggest operational risk -- when it fails (approximately twice per month), the warehouse operations team works the next day with stale inventory data, occasionally shipping expired or recalled products because the recall status had not propagated.

The Chief Technology Officer (CTO) has mandated a migration to Databricks with three hard requirements. First, inventory data must be updated within 15 minutes of any change, eliminating the nightly batch dependency. Second, every data transformation must be auditable for Food and Drug Administration (FDA) compliance -- regulators must be able to trace any shipped product back through the data pipeline to the original source record. Third, the system must enforce data quality gates that prevent recalled products from appearing as available in the ordering system. A recalled product reaching a hospital is a patient safety incident and a potential multi-million dollar liability.

Your team consists of two junior data engineers (who completed a course similar to this one) and a data analyst who writes Structured Query Language (SQL). The legacy Oracle database will continue to operate during the migration, with Change Data Capture (CDC) replication streaming changes to a Kafka cluster. Manufacturer data arrives as daily Comma-Separated Values (CSV) files dropped into a Secure File Transfer Protocol (SFTP) server. Hospital purchase orders come through an Electronic Data Interchange (EDI) integration that writes JSON files to cloud storage. Product recall notices arrive as structured Extensible Markup Language (XML) from the FDA's openFDA Application Programming Interface (API), polled every 5 minutes.

## Tasks

### Task 1: Design the Complete Pipeline Architecture

Define every layer of the medallion architecture for MedSupply's inventory management system. For the bronze layer, specify how each of the four data sources (Oracle CDC via Kafka, manufacturer CSVs, hospital EDI JSON, FDA recall XML) will be ingested. For the silver layer, define the conformed data model including the `inventory_current` table (Slowly Changing Dimension Type 1 via `apply_changes()`), the `inventory_history` table (SCD Type 2 for audit trail), and the `product_recall_status` table. For the gold layer, define the `warehouse_availability` table that powers the ordering system and the `compliance_audit_trail` table that satisfies FDA requirements. Specify the CDC keys, sequence columns, and `apply_changes()` configurations for each table that uses CDC.

### Task 2: Implement Data Quality Gates for Patient Safety

Design the expectations that prevent recalled products from being marked as available. This requires a multi-table quality gate: the `warehouse_availability` gold table must join against `product_recall_status` and enforce that no row has `recall_status = 'active'` with `availability = 'in_stock'`. Define this as a FAIL UPDATE expectation and explain what happens operationally when it fires -- who gets paged, what is the fallback process, and how does the warehouse team continue operating while the data team investigates. Additionally, define expectations at the silver layer for each source: valid National Drug Classification (NDC) codes, non-negative quantities, timestamps within a reasonable range, and referential integrity between purchase orders and known hospital identifiers.

### Task 3: Plan the Migration and Team Execution

Create a phased migration plan that your two junior engineers and SQL analyst can execute over 12 weeks. Phase 1 should establish the bronze layer and validate that CDC replication matches the Oracle source (run both systems in parallel and compare). Phase 2 should build the silver and gold layers with expectations, using the legacy system as the source of truth for validation. Phase 3 should cut over the ordering system to read from the Databricks gold table instead of Oracle, with a rollback plan. For each phase, assign specific tasks to team members based on their skill levels, define the acceptance criteria, and identify the risks. Explain how you will use the DLT event log to build a monitoring dashboard that gives the warehouse operations team confidence in the new system before cutover.

## AI Persona

**Title**: Chief Technology Officer

**Overview**: A veteran technology executive with deep experience in regulated industries (healthcare, finance). They understand both the technical complexity and the regulatory stakes of the migration. They will challenge your team capacity estimates, probe your rollback strategy, and insist on concrete acceptance criteria for each phase. They are supportive but demanding -- they need to defend this migration plan to the board and the FDA compliance team.

## Evaluation Criteria

### Advanced

- The `apply_changes()` configurations are correct and complete with keys, sequence columns, SCD type, and delete conditions specified for each CDC-driven table
- The critical recall-availability cross-check uses FAIL UPDATE to halt the pipeline with a realistic operational response plan including alerting, fallback procedures, and escalation path
- The 12-week migration plan is realistic for the team's skill composition with appropriately scoped tasks, parallel-run validation, and specific risk mitigations
- Monitoring dashboard design demonstrates that observability is built into the migration from day one

### Intermediate

- Correctly identifies the four data sources and assigns appropriate ingestion methods for each in the bronze layer
- Defines SCD Type 1 and Type 2 tables with reasonable `apply_changes()` configurations but may miss edge cases in CDC ordering
- Data quality expectations address the patient safety requirement at a conceptual level
- Migration plan has clear phases but may underestimate complexity or lack specific acceptance criteria

### Beginner

- Demonstrates understanding of the medallion architecture and can outline a bronze-silver-gold structure for the scenario
- Attempts CDC configuration but may confuse SCD types or omit key parameters in `apply_changes()`
- Recognizes the patient safety requirement but proposes expectations that may not fully prevent recalled products from propagating
- Migration plan exists but may not account for team skill levels or parallel-run validation
