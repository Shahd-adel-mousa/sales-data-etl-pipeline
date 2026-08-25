# Sales Data ETL Pipeline

A beginner-friendly ETL pipeline built with Python and Pandas to extract, validate, clean, transform, and load sales data.

## Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using a sales dataset stored in CSV format.

The pipeline validates the input data, removes duplicate and missing records, calculates total sales, and saves the processed data into a new CSV file.

## Technologies Used

* Python
* Pandas
* CSV
* Git & GitHub

## ETL Process

### 1. Extract

The pipeline reads the raw sales data from:

`data/sales_data.csv`

### 2. Validate

The pipeline checks that:

* All required columns are available.
* `Quantity` contains numeric values.
* `Unit_Price` contains numeric values.
* `Quantity` and `Unit_Price` contain positive values.

### 3. Transform

The data is processed by:

* Removing duplicate records.
* Removing missing values.
* Calculating `Total_Sales`.

The total sales value is calculated using:

`Total_Sales = Quantity × Unit_Price`

### 4. Load

The processed data is saved to:

`data/processed_sales_data.csv`

## Project Structure

```text
sales-data-etl-pipeline/
│
├── data/
│   ├── sales_data.csv
│   └── processed_sales_data.csv
│
├── etl_pipeline.py
├── requirements.txt
└── README.md
```

## How to Run

Install the required dependency:

```bash
pip install -r requirements.txt
```

Run the ETL pipeline:

```bash
python etl_pipeline.py
```

## Expected Output

```text
Starting ETL pipeline...
Extracted 8 records.
Data transformation completed.
Processed 8 records.
Output saved to: data/processed_sales_data.csv
ETL pipeline completed successfully!
```

## Learning Goals

This project was created to practice:

* Python
* Pandas
* Data Cleaning
* Data Validation
* Data Transformation
* ETL Pipeline Fundamentals
* Basic Data Engineering Concepts
* Git & GitHub

