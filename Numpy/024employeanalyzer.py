# Employee Attendance and Performance Analyzer
# Goal: Force you to replace Python loops with NumPy operations.

# Dataset
# You are given weekly attendance and performance scores for employees.
# Rows = employees
# Columns = weeks

# Data contains:
# • integers
# • floats
# • None
# • invalid strings

# Your job is to clean, analyze, and summarize using NumPy.
# Data
# attendance_scores = [
# [8, 9, 7, None, 10],
# [6, "A", 7, 8, 7],
# [10, 10, 9, 6, None],
# [9, 8, 8, 9, "X"]
# ]

# Requirements
# You must return a dictionary with the following keys.
# clean_array
# 2D NumPy array. dtype float.
# Invalid values replaced with np.nan.
# employee_averages
# 1D NumPy array.
# Average score per employee. Ignore NaNs.
# week_averages
# 1D NumPy array.
# Average score per week. Ignore NaNs.
# top_employee_index
# Index of highest employee average.
# bottom_employee_index
# Index of lowest employee average.
# attendance_rate
# Single float.
# Percentage of valid entries over total possible entries.
# Example: 0.84
# performance_tiers
# Python dict using vectorized counting. No loops.
# Keys:
# • "Low < 7"
# • "Mid 7–8.9"
# • "High >= 9"

# Counts all valid scores.
# Rules
# • Use NumPy for calculations
# • No nested loops for analysis
# • Cleaning loop is allowed
# • Use boolean masks
# • Use np.nanmean
# • Use np.isnan
# • Use np.count_nonzero

import numpy as np 

attendance_scores = [
[8, 9, 7, None, 10],
[6, "A", 7, 8, 7],
[10, 10, 9, 6, None],
[9, 8, 8, 9, "X"]
]

def employee_analyzer(attendance_scores):
    
    cleaned_attendance_scores: list = []
    for row in attendance_scores:
        cleaned_attendance_rows: list = []
        for score in row:
            if isinstance(score, (int, float)):
                cleaned_attendance_rows.append(score)
            else:
                cleaned_attendance_rows.append(np.nan)
        cleaned_attendance_scores.append(cleaned_attendance_rows)

    attendance_scores_array = np.array(cleaned_attendance_scores, dtype=float)

    employee_averages = np.nanmean(attendance_scores_array, axis=1)
    week_averages = np.nanmean(attendance_scores_array, axis=0)
    top_employee_index = np.nanargmax(employee_averages)
    bottom_employee_index = np.nanargmin(employee_averages)

    valid_count = np.count_nonzero(~np.isnan(attendance_scores_array))
    total_count = attendance_scores_array.size
    attendance_rate = valid_count / total_count

    performance_tiers = {
        "Low < 7": int(np.sum(attendance_scores_array < 7)),
        "Mid 7–8.9": int(np.sum((7 < attendance_scores_array) & (attendance_scores_array < 9))),
        "High >= 9": int(np.sum(attendance_scores_array >= 9))
    }

    return {
        "attendance_scores_array": attendance_scores_array,
        "employee_averages": employee_averages,
        "week_averages": week_averages,
        "top_employee_index": top_employee_index,
        "bottom_employee_index": bottom_employee_index,
        "attendance_rate": attendance_rate,
        "performance_tiers": performance_tiers
    }

def main():
    result = employee_analyzer(attendance_scores)
    print(f"Cleaned Array:\n{result['attendance_scores_array']}")
    print(f"Employee Averages:{result['employee_averages']}")
    print(f"Week Averages:{result['week_averages']}")
    print(f"Top Employee Index:{result['top_employee_index']}")
    print(f"Bottom Employee Index:{result['bottom_employee_index']}")
    print(f"Attendance Rate:{result['attendance_rate']}")
    print(f"Performance Tiers:{result['performance_tiers']}")

if __name__ == "__main__":
    main()

#1/9/2026 grade 92/100