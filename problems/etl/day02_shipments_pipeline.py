import pandas as pd

# Extract
data = [
  {"shipment_id": "S001", "courier": "fedex", "weight_kg": 2.5, "status": "delivered", "date": "2024-01-15"},
  {"shipment_id": "S002", "courier": "UPS", "weight_kg": None, "status": "in_transit", "date": "2024-01-15"},
  {"shipment_id": "S003", "courier": "dhl", "weight_kg": 5.0, "status": "delivered", "date": "not-a-date"},
  {"shipment_id": "S004", "courier": "FedEx", "weight_kg": 1.2, "status": "pending", "date": "2024-01-16"},
  {"shipment_id": "S005", "courier": "ups", "weight_kg": 3.8, "status": "delivered", "date": "2024-01-16"}
]

df = pd.DataFrame(data)

# Transform
# 1. Standardize courier to uppercase
df['courier'] = df['courier'].str.upper()

# 2. Drop rows where weight_kg is missing
df = df.dropna(subset=['weight_kg'])

# 3. Convert date to datetime, bad dates become NaT
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Load
df.to_csv('shipments.csv', index=False)

print("ETL complete!")
print(df)
