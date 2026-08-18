# Pandas Project 2: Transaction Analysis & Filtering

# Practice:
# Boolean masking
# Creating new columns
# Aggregations
# Sorting and filtering
# Returning structured results

# Dataset
# transactions = [
#     {"user": "Ava", "amount": 120.5, "category": "food", "status": "completed"},
#     {"user": "Ben", "amount": None, "category": "travel", "status": "completed"},
#     {"user": "Ava", "amount": "ERR", "category": "food", "status": "failed"},
#     {"user": "Cara", "amount": 300, "category": "rent", "status": "completed"},
#     {"user": "Ben", "amount": "200", "category": "food", "status": "completed"},
#     {"user": "", "amount": 50, "category": "misc", "status": "completed"},
# ]

# Your Task
# Write a function called:
# def analyze_transactions(transactions: list[dict]) -> dict:

# Required Steps
# Convert transactions into a DataFrame.
# Replace empty strings with NaN.
# Convert amount to numeric using pd.to_numeric(errors="coerce").
# Drop rows where:
# user is missing
# OR amount is missing
# Create a new column:
# fee = amount * 0.05
# Keep only rows where status == "completed".

# Compute:
# Total amount per user
# Average amount per category
# Sort users by total amount (descending).
# Return Value

# Your function must return:
# {
#     "cleaned_df": <DataFrame>,
#     "total_by_user": <Series>,
#     "avg_by_category": <Series>
# }

# Rules
# No loops
# No .iterrows()
# Use Pandas operations only
# Clean, readable code

import pandas as pd
import numpy as np

transactions = [
    {"user": "Ava", "amount": 120.5, "category": "food", "status": "completed"},
    {"user": "Ben", "amount": None, "category": "travel", "status": "completed"},
    {"user": "Ava", "amount": "ERR", "category": "food", "status": "failed"},
    {"user": "Cara", "amount": 300, "category": "rent", "status": "completed"},
    {"user": "Ben", "amount": "200", "category": "food", "status": "completed"},
    {"user": "Ben", "amount": "520", "category": "food", "status": "completed"},
    {"user": "", "amount": 50, "category": "misc", "status": "completed"},
]

def analyze_transactions(transactions: list[dict]) -> dict:
    
    df = pd.DataFrame(transactions)
    df.replace("", np.nan, inplace=True)
    df["amount"] = df["amount"].apply(
        pd.to_numeric,
        errors="coerce")
    df.dropna(subset=["user", "amount"], inplace=True)
    df["fee"] = df["amount"] * 0.05
    filtered_df = df[df["status"] == "completed"]

    total_by_user = round(filtered_df.groupby("user")["amount"].agg("sum"), 2)
    avg_by_category = filtered_df.groupby("category")["amount"].agg("mean").round(2)

    return {
    "cleaned_df": filtered_df,
    "total_by_user": total_by_user,
    "avg_by_category": avg_by_category
}

def main():
    rs = analyze_transactions(transactions)
    print(f"{rs["cleaned_df"]}\n{rs["total_by_user"]}\n{rs["avg_by_category"]}")

if __name__ == "__main__":
    main()