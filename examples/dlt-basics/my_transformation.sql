-- Delta Live Tables: Bronze-Silver-Gold pipeline in SQL
-- This example demonstrates the medallion architecture using inline data.
-- Run this as a DLT pipeline in your Databricks workspace.

-- BRONZE
CREATE LIVE TABLE customers_raw AS
SELECT * FROM VALUES
  (1, 'Alice', 'alice@email.com', 25),
  (2, 'Bob', NULL, 30),
  (3, 'Charlie', 'charlie@email.com', -5)
AS (id, name, email, age);

-- SILVER
CREATE LIVE TABLE customers_clean (
  CONSTRAINT valid_email EXPECT (email IS NOT NULL) ON VIOLATION DROP ROW,
  CONSTRAINT valid_age EXPECT (age > 0) ON VIOLATION DROP ROW
) AS
SELECT * FROM LIVE.customers_raw;

-- GOLD
CREATE LIVE TABLE age_by_initial AS
SELECT
  substring(name, 1, 1) AS initial,
  avg(age) AS avg_age
FROM LIVE.customers_clean
GROUP BY initial;
