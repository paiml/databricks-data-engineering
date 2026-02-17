# Delta Live Tables: Bronze and Silver layers for wine data
# This pipeline ingests raw wine data and cleans it in the silver layer.
#
# IMPORTANT: Update the CSV path below to match YOUR Databricks workspace volumes.
# The path references /Volumes/workspace/default/raw/ which may differ in your setup.

import dlt
from pyspark.sql.functions import col, regexp_replace, trim

@dlt.table(
    name="wine_bronze",
    comment="Raw wine data ingested from volume"
)
def wine_bronze():
    return (
        spark.read.csv(
            "/Volumes/workspace/default/raw/wine-ratings.csv",
            header=True,
            inferSchema=True,
            escape='"'
        )
    )

@dlt.table(
    name="wine_silver",
    comment="Cleaned and validated wine data"
)
@dlt.expect_or_drop("valid_rating", "rating IS NOT NULL")
def wine_silver():
    return (
        dlt.read("wine_bronze")
        .withColumn("name", regexp_replace(col("name"), "[\r\n]+", " "))
        .withColumn("region", regexp_replace(col("region"), "[\r\n]+", " "))
        .withColumn("variety", regexp_replace(col("variety"), "[\r\n]+", " "))
        .withColumn("notes", regexp_replace(col("notes"), "[\r\n]+", " "))
        .withColumn("name", trim(col("name")))
        .withColumn("region", trim(col("region")))
        .withColumn("variety", trim(col("variety")))
        .withColumn("notes", trim(col("notes")))
        .drop("grape")
        .dropDuplicates()
    )
