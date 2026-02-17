# Delta Live Tables: Batch vs Streaming ingestion
# This example shows how to read data in batch mode and streaming mode
# using Auto Loader (cloudFiles).
#
# IMPORTANT: Update the paths below to match YOUR Databricks workspace volumes.
# The paths reference /Volumes/workspace/default/ which may differ in your setup.

import dlt
from pyspark.sql.types import *

# Define the schema
customer_schema = StructType([
  StructField("id", IntegerType(), True),
  StructField("name", StringType(), True),
  StructField("amount", IntegerType(), True)
])

@dlt.table
def customers_batch():
  return spark.read.csv("/Volumes/workspace/default/streaming", header=True)

#@dlt.table
#def customers_streaming():
#  return spark.readStream.schema(customer_schema).csv(
#      "/Volumes/workspace/default/streaming",
#      header=True)

@dlt.table
def customers_streaming():
  return (
    spark.readStream
      .format("cloudFiles")  # Auto Loader magic
      .option("cloudFiles.format", "csv")
      .option("cloudFiles.schemaLocation", "/Volumes/workspace/default/raw")  # Stores inferred schema
     .option("cloudFiles.inferColumnTypes", "true")
      .option("header", "true")
      .load("/Volumes/workspace/default/streaming")
  )
