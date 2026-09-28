import polars as pl

df = pl.read_csv("chicago-ward-income.csv")
print(df)
