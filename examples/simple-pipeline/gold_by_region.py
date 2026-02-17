# Delta Live Tables: Gold layer aggregations
# Creates business-ready tables from the cleaned silver layer.
# Requires the silver layer from bronze.py to be running in the same pipeline.

import dlt
from pyspark.sql.functions import col, count, avg

@dlt.table(name="wine_gold_top_rated",
               table_properties={"quality": "gold"}

           )
def wine_gold_top_rated():
    return dlt.read_stream("wine_silver").filter(col("rating") >= 90)

@dlt.table(name="wine_gold_by_region",
               table_properties={"quality": "gold"}
           )
def wine_gold_by_region():
    return dlt.read_stream("wine_silver").groupBy("region").agg(
        count("*").alias("wine_count"),
        avg("rating").alias("avg_rating")
    )
