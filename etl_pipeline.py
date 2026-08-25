import pandas as pd

# Extract
df = pd.read_csv("data/sales_data.csv")

# Transform
df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

df = df.drop_duplicates()
df = df.dropna()

# Load
df.to_csv("data/processed_sales_data.csv", index=False)

print("ETL pipeline completed successfully!")
print(df)
