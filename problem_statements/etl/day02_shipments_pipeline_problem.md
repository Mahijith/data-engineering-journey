# Day 2 — ETL: Shipments Pipeline

## Category
ETL (Extract, Transform, Load)

## Level
Beginner

## Problem Statement
You work at a logistics company. Every day a JSON file is dropped into a folder containing shipment records from different couriers. Your job is to build a simple ETL pipeline that extracts, transforms, and loads the data into a clean CSV file ready for the analytics team.

## Raw Data
```json
[
  {"shipment_id": "S001", "courier": "fedex", "weight_kg": 2.5, "status": "delivered", "date": "2024-01-15"},
  {"shipment_id": "S002", "courier": "UPS", "weight_kg": null, "status": "in_transit", "date": "2024-01-15"},
  {"shipment_id": "S003", "courier": "dhl", "weight_kg": 5.0, "status": "delivered", "date": "not-a-date"},
  {"shipment_id": "S004", "courier": "FedEx", "weight_kg": 1.2, "status": "pending", "date": "2024-01-16"},
  {"shipment_id": "S005", "courier": "ups", "weight_kg": 3.8, "status": "delivered", "date": "2024-01-16"}
]
```

## Task
Write a Python script that:
1. **Extracts** — loads the JSON data into a pandas DataFrame
2. **Transforms** — applies these rules:
   - Standardize the `courier` column to uppercase (fedex, FedEx → FEDEX)
   - Drop rows where `weight_kg` is missing
   - Convert `date` to a proper datetime — bad dates become `NaT`
3. **Loads** — saves the cleaned DataFrame to `shipments.csv` without the index

## Key Concepts Learned
- ETL stands for Extract, Transform, Load — the fundamental data engineering pattern
- `pd.DataFrame(data)` — create a DataFrame from a Python list of dicts
- `df['col'].str.upper()` — standardize string columns to uppercase
- Always separate extraction, transformation, and loading into distinct steps
- The load step should always be the last step after all transformations are complete

## Solution File
`day02_shipments_pipeline.py`
