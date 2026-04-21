import pandas as pd
from io import StringIO

raw = """ transaction_id , customer_id , amount , sale_date
1001, C001, 59.99, 2024-01-15
1003, C003, 120.50, not-a-date
1005, C005, 45.00, 2024-01-16
1006, C006, 200.00, 2024-01-17
1008, C008, 33.75, bad-date
1009, , 78.00, 2024-01-18
1010, C010, 15.50, 2024-01-18"""

df = pd.read_csv(StringIO(raw))
df.columns = df.columns.str.strip()
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')
df = df.dropna(subset=['amount'])
df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')

# Save to CSV without index
df.to_csv('cleaned_transactions.csv', index=False)

# Save to JSON with records orientation
df.to_json('cleaned_transactions.json', orient='records')

print("Files saved successfully!")
print(df)
