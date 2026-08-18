# Pandas Project 1 — DataFrame Builder & Cleaner
# This project is simple on the surface. It is not easy if done correctly.
# Goal
# Take messy raw data and turn it into a clean, usable Pandas DataFrame.
# This mirrors real data ingestion.
# Input Data

# You are given raw records with:
# • Mixed types
# • Missing values
# • Invalid numeric entries

# Use exactly this data.

# raw_data = [
#     {"name": "Alice", "age": "25", "score": 90},
#     {"name": "Bob", "age": 22, "score": "85"},
#     {"name": "Charlie", "age": None, "score": "ERR"},
#     {"name": "Dana", "age": "N/A", "score": 88},
#     {"name": "Evan", "age": 19, "score": None},
#     {"name": "", "age": 21, "score": 75}
# ]

# Requirements
# Write a function:
# def dataframe_cleaner(raw_data: list[dict]) -> dict:

# Tasks
# Create a Pandas DataFrame from raw_data

# Clean the data
# • Empty names become NaN
# • Convert age and score to numeric
# • Invalid values become NaN

# Do not drop rows yet
# Compute and return:
# • Cleaned DataFrame
# • Missing value count per column
# • Data types of each column

# Output Format
# Return one dictionary:
# {
#     "cleaned_df": <DataFrame>,
#     "missing_counts": <Series or dict>,
#     "dtypes": <Series or dict>
# }

# Constraints
# • Use Pandas operations only
# • No loops for cleaning
# • No hardcoding column names
# • Defensive logic

# What This Tests
# • DataFrame creation
# • to_numeric
# • isna
# • dtype awareness
# • Vectorized thinking

import pandas as pd
import numpy as np

raw_data = [
    {"name": "Alice", "age": "25", "score": 90},
    {"name": "Bob", "age": 22, "score": "85"},
    {"name": "Charlie", "age": None, "score": "ERR"},
    {"name": "Dana", "age": "N/A", "score": 88},
    {"name": "Evan", "age": 19, "score": None},
    {"name": "", "age": 21, "score": 75}
]

def dataframe_cleaner(raw_data: list[dict]) -> dict:
    df = pd.DataFrame(raw_data)

    # Empty strings → NaN
    df.replace("", np.nan,inplace=True)

    # Convert all non-name columns to numeric
    non_name_cols = df.columns.difference(["name"]) #calls all columns in the dataframe and .difference(["name"]) calls on all columns except name
    df[non_name_cols] = df[non_name_cols].apply( #all other columns and attempts conversion to numeric
        pd.to_numeric, errors="coerce" #errors="coerce" is important
    )

    #if conversion fails -> replace with NaN

    missing_counts = df.isna().sum()
    dtypes = df.dtypes

    return {
        "cleaned_df": df,
        "missing_counts": missing_counts,
        "dtypes": dtypes
    }

def main():
    result = dataframe_cleaner(raw_data)
    print("Cleaned DataFrame:\n", result["cleaned_df"])
    print("\nMissing Counts:\n", result["missing_counts"])
    print("\nDtypes:\n", result["dtypes"])

if __name__ == "__main__":
    main()