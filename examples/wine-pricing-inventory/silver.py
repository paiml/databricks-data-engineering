# Delta Live Tables: Silver layer for wine pricing inventory
# Cleans and validates wine catalog data and price updates.
# Uses expectations to enforce data quality constraints.

import dlt
from pyspark.sql.functions import col

@dlt.table(
    comment="Cleaned wine catalog"
)
@dlt.expect_or_drop("valid_price", "price > 0")
def silver_wines():
    return (
        dlt.read("bronze_wines")
        .select("name", "region", "variety", "rating", "price", "notes")
    )

@dlt.table(
    comment="Validated price updates"
)
@dlt.expect_or_fail("valid_price_update", "price > 0")
def silver_price_updates():
    return (
        dlt.read_stream("bronze_price_updates")
        .select(
            col("wine_name").alias("name"),  # Rename to match silver_wines
            "price",
            col("effective_date").cast("date")
        )
    )
