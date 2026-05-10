# NUMPY PROJECT 2 Title: Sales Performance Analyzer
# Goal
# Practice vectorized NumPy operations. No Python loops for calculations.

# Dataset
# You are given raw sales data for multiple sales reps across several months.
# sales = [
# [1200, 1500, None, 1800, 2000],
# [800, 950, 1100, "N/A", 1300],
# [2000, 2100, 2200, 2300, 2400],
# [None, 700, 650, 600, 580],
# [1600, 1700, 1650, 1750, None]
# ]

# Requirements
# Write a function called sales_analyzer(sales) that returns a dictionary with:
# "clean_array": 2D NumPy array of floats. Convert invalid values to np.nan
# "rep_averages": 1D NumPy array Average sales per rep using np.nanmean
# "month_averages": 1D NumPy array Average sales per month using np.nanmean
# "top_rep_index": Index of rep with highest average
# "bottom_rep_index": Index of rep with lowest average
# "overall_growth_rate": Single float
# Formula: (last_month_avg − first_month_avg) / first_month_avg (Round to 2 decimals)
# "performance_distribution"
# Python dict with keys:
# "Low" < 1000
# "Mid" 1000–1799
# "High" ≥ 1800
# Count all valid sales values.

# Rules
# • Use np.nan, np.nanmean, np.nanargmax, np.nanargmin
# • No manual loops for averages or rankings
# • One loop allowed for distribution only
# • Clean, readable code

import numpy as np

sales = [
[1200, 1500, None, 1800, 2000],
[800, 950, 1100, "N/A", 1300],
[2000, 2100, 2200, 2300, 2400],
[None, 700, 650, 600, 580],
[1600, 1700, 1650, 1750, None]
]

def sales_performance_analzyzer(sales):
    
    cleaned_sales: list = []
    for row in sales:
        cleaned_sales_row: list = []
        for sale in row:
            if isinstance(sale, (int, float)):
                cleaned_sales_row.append(sale)
            else:
                cleaned_sales_row.append(np.nan)
        cleaned_sales.append(cleaned_sales_row)
    
    cleaned_sales_array = np.array(cleaned_sales, dtype=float)

    rep_averages = np.nanmean(cleaned_sales_array, axis=1)

    month_averages = np.nanmean(cleaned_sales_array, axis=0)

    top_rep_index = np.nanargmax(rep_averages)

    bottom_rep_index = np.nanargmin(rep_averages)

    first_month_average = month_averages[0]
    last_month_average = month_averages[-1]
    overall_growth_rate = (last_month_average - first_month_average) / first_month_average

    performance_distribution = {
        "Low < 1000": 0,
        "Mid 1000–1799": 0,
        "High(>= 1800)": 0
    }

    all_sales = cleaned_sales_array.flatten()
    all_sales = all_sales[~np.isnan(all_sales)]

    for sale in all_sales:
        if sale < 1000:
            performance_distribution["Low < 1000"] += 1
        elif 1000 <= sale <= 1799:
            performance_distribution["Mid 1000–1799"] += 1
        elif sale >= 1800:
            performance_distribution["High(>= 1800)"] += 1

    return {
        "cleaned_array": cleaned_sales_array,
        "rep_averages": rep_averages,
        "month_averages": month_averages,
        "top_rep_index": top_rep_index,
        "bottom_rep_index": bottom_rep_index,
        "overall_growth_rate": overall_growth_rate,
        "performance_distribution": performance_distribution
    }

def main():
    result = sales_performance_analzyzer(sales)
    print(f"Cleaned Array:\n{result['cleaned_array']}")
    print(f"Representative Averages: {result['rep_averages']}")
    print(f"Month Averages: {result['month_averages']}")
    print(f"Top Rep Index: {result['top_rep_index']}")
    print(f"Bottom Rep Index: {result['bottom_rep_index']}")
    print(f"Overall Growth Rate: {result['overall_growth_rate']}")
    print(f"Performance Distribution: {result['performance_distribution']}")
    


if __name__ == "__main__":
    main()

#1/9/2026 92/100