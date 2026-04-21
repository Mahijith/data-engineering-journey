import pandas as pd
from io import StringIO

raw = """ transaction_id , customer_id , amount , sale_date
1001, C001, 59.99, 2024-01-15
1002, C002, , 2024-01-15
1003, C003, 120.50, not-a-date
1004, , 89.00, 2024-01-16
1005, C005, 45.00, 2024-01-16
1006, C006, 200.00, 2024-01-17
1007, C007, , 2024-01-17
1008, C008, 33.75, bad-date
1009, , 78.00, 2024-01-18
1010, C010, 15.50, 2024-01-18"""

df = pd.read_csv(StringIO(raw))

# Step 2: Strip whitespace from column names
df.columns = df.columns.str.strip()

# Step 3: Convert amount to numeric so empty strings become NaN
df['amount'] = pd.to_numeric(df['amount'], errors='coerce')

# Step 4: Drop rows where amount is missing
df = df.dropna(subset=['amount'])

# Step 5: Convert sale_date to datetime, bad dates become NaT
df['sale_date'] = pd.to_datetime(df['sale_date'], errors='coerce')

print(df)
