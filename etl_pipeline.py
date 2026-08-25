import pandas as pd

INPUT_FILE = "data/sales_data.csv"
OUTPUT_FILE = "data/processed_sales_data.csv"

try:
    # Extract
    print("Starting ETL pipeline...")
    df = pd.read_csv(INPUT_FILE)
    print(f"Extracted {len(df)} records.")

    # Transform
    df = df.drop_duplicates()
    df = df.dropna()

    df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

    # Load
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Successfully loaded {len(df)} processed records.")
    print(f"Output saved to: {OUTPUT_FILE}")

except FileNotFoundError:
    print(f"Error: Input file not found: {INPUT_FILE}")

except Exception as e:
    print(f"ETL pipeline failed: {e}")
