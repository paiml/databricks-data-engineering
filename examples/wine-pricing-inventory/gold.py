# Delta Live Tables: Gold layer with Change Data Capture (CDC)
# Implements SCD Type 1 (current prices) and SCD Type 2 (full price history)
# using dlt.apply_changes() for tracking price changes over time.

import dlt

# Current prices only
dlt.create_streaming_table("gold_current_prices")

dlt.apply_changes(
    target="gold_current_prices",
    source="silver_price_updates",
    keys=["name"],
    sequence_by="effective_date",
    stored_as_scd_type=1
)

# Full price history
dlt.create_streaming_table("gold_price_history")

dlt.apply_changes(
    target="gold_price_history",
    source="silver_price_updates",
    keys=["name"],
    sequence_by="effective_date",
    stored_as_scd_type=2
)
