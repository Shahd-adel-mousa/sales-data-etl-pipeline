
import pandas as pd

INPUT_FILE = "data/sales_data.csv"
OUTPUT_FILE = "data/processed_sales_data.csv"


def run_etl():
    print("Starting ETL pipeline...")

    # Extract
    df = pd.read_csv(INPUT_FILE)
    print(f"Extracted {len(df)} records.")

    # Validate required columns
    required_columns = [
        "Order_ID",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price",
        "Region"
    ]

    missing_columns = set(required_columns) - set(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    # Validate numeric columns
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
    df["Unit_Price"] = pd.to_numeric(df["Unit_Price"], errors="coerce")

    # Remove duplicates and missing values
    df = df.drop_duplicates()
    df = df.dropna()

    # Validate positive values
    if (df["Quantity"] <= 0).any():
        raise ValueError("Quantity must contain positive values.")

    if (df["Unit_Price"] <= 0).any():
        raise ValueError("Unit_Price must contain positive values.")

    # Transform
    df["Total_Sales"] = df["Quantity"] * df["Unit_Price"]

    print("Data transformation completed.")

    # Load
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Processed {len(df)} records.")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    try:
        run_etl()
        print("ETL pipeline completed successfully!")

    except FileNotFoundError:
        print(f"Error: Input file not found: {INPUT_FILE}")

    except ValueError as e:
        print(f"Data validation error: {e}")

    except Exception as e:
        print(f"ETL pipeline failed: {e}")
