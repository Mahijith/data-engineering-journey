import pandas as pd

# Extract
data = [
  {"transaction_id": "T001", "branch_code": "NYC", "amount": 1500.00, "date": "2024-01-15"},
  {"transaction_id": "T002", "branch_code": "CHI", "amount": -200.00, "date": "2024-01-15"},
  {"transaction_id": "T003", "branch_code": "NY",  "amount": 850.00,  "date": "2024-01-15"},
  {"transaction_id": "T001", "branch_code": "HOU", "amount": 3200.00, "date": "2024-01-16"},
  {"transaction_id": "T005", "branch_code": "CHI", "amount": 950.00,  "date": "2024-01-16"},
  {"transaction_id": "T006", "branch_code": "NYC", "amount": 0.00,    "date": "2024-01-16"},
  {"transaction_id": "T007", "branch_code": None,  "amount": 1100.00, "date": "2024-01-16"},
  {"transaction_id": "T008", "branch_code": "LAX", "amount": 2200.00, "date": "2024-01-17"}
]
df = pd.DataFrame(data)

# Data Quality Checks
# Check 1: Missing critical values
missing_mask = df[["transaction_id", "branch_code", "amount"]].isnull().any(axis=1)

# Check 2: Duplicate transaction_id
duplicate_mask = df.duplicated(subset=["transaction_id"], keep=False)

# Check 3: Invalid amount (zero or negative)
amount_mask = df["amount"] <= 0

# Check 4: Invalid branch_code (not exactly 3 characters)
branch_mask = df['branch_code'].str.len().fillna(0) != 3

# Combine all failed masks
failed_mask = missing_mask | duplicate_mask | amount_mask | branch_mask

# Assign failure reasons
def get_failure_reason(row):
    reasons = []
    if missing_mask[row.name]:   reasons.append("missing critical value")
    if duplicate_mask[row.name]: reasons.append("duplicate transaction_id")
    if amount_mask[row.name]:    reasons.append("invalid amount")
    if branch_mask[row.name]:    reasons.append("invalid branch_code")
    return " | ".join(reasons)

# Split into clean and quarantine
quarantine_df = df[failed_mask].copy()
quarantine_df['failure_reason'] = quarantine_df.apply(get_failure_reason, axis=1)
clean_df = df[~failed_mask].copy()

# Load
clean_df.to_csv('clean_transactions.csv', index=False)
quarantine_df.to_csv('quarantine_transactions.csv', index=False)

print(f"Clean rows: {len(clean_df)}")
print(f"Quarantined rows: {len(quarantine_df)}")
print("\nClean data:")
print(clean_df)
print("\nQuarantined data:")
print(quarantine_df)
