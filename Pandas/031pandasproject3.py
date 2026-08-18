# Pandas Project 3 — Sales Performance Analyzer

# 1. Clean the data
# • Replace empty strings with NaN
# • Convert sales and units to numeric
# • Drop rows where rep or sales is missing

# 2. Create a new column
# avg_price = sales / units



# {
#     "cleaned_df": <DataFrame>,
#     "summary_table": <DataFrame>
# }
# The summary table must include:
# region
# rep
# total_sales
# total_units
# avg_price_mean
# rank

import pandas as pd
import numpy as np

sales_data = [
    {"region": "North", "rep": "Alice", "sales": 500, "units": 5},
    {"region": "North", "rep": "Bob", "sales": 300, "units": 3},
    {"region": "South", "rep": "Alice", "sales": 700, "units": 7},
    {"region": "South", "rep": "Cara", "sales": 400, "units": 4},
    {"region": "East", "rep": "Bob", "sales": 600, "units": 6},
    {"region": "East", "rep": "Cara", "sales": None, "units": 2},
    {"region": "West", "rep": "", "sales": 200, "units": 1},
]


def analyze_sales(sales_data: list[dict]) -> dict:

    df = pd.DataFrame(sales_data)
    df.replace("", np.nan, inplace=True)
    df["sales"] = df[("sales")].apply(
        pd.to_numeric,
        errors="coerce"
    )
    df["units"] = df[("units")].apply(
        pd.to_numeric,
        errors="coerce"
    )
    df.dropna(subset=("rep", "sales"), inplace=True)

    df["avg_price"] = df["sales"] / df["units"]

# 3. Multi-column groupby
# Group by:
# ["region", "rep"]
# Compute ALL of these at once:
# • total_sales → sum of sales
# • total_units → sum of units
# • avg_price_mean → mean of avg_price
# You must use .agg() with a dictionary.
# 4. Sort results
# Sort by:
# total_sales descending
    summary_table = df.groupby(["region", "rep"]).agg({
        "sales": "sum",
        "units": "sum",
        "avg_price": "mean"
    }).rename(columns={
        "sales": "total_sales",
        "units": "total_units",
        "avg_price": "avg_price_mean"
    }).sort_values(by="total_sales", ascending=False)
    summary_table.reset_index()

# 5. Add a ranking column
# Rank reps by total_sales:
# • Highest sales = rank 1
# • No ties expected
# • Dense ranking preferred

    summary_table["sales_rank"] = summary_table["total_sales"].rank(method="dense", ascending=False).astype(int)
    summary_table = summary_table.sort_values(by="sales_rank")


    return {
    "cleaned_df": df,
    "summary_table": summary_table
}

def main():
    result = analyze_sales(sales_data)
    print(result["cleaned_df"])
    print(result["summary_table"])

if __name__ == "__main__":
    main()

#3/24/2026 Grade 94/100