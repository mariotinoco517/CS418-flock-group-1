import json
import polars as pl

# Use open() and json.load() for files
with open("cameras.geojson", "r", encoding="utf-8") as f:
    geojson_data = json.load(f)

extracted_df = (
    pl.from_dicts(geojson_data["features"])
    .with_columns(
        longitude=pl.col("geometry").struct.field("coordinates").list.get(0),
        latitude=pl.col("geometry").struct.field("coordinates").list.get(1),
    )
    .unnest("properties")
    .drop("type", "geometry")
)

print(extracted_df)
