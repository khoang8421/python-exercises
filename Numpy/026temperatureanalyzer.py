# NumPy Project 5 — Temperature Trend Analyzer

# Goal
# Analyze temperature readings over time and detect trends and volatility using NumPy.

# Input
# A 2D list.
# Each row = one city.
# Each column = one day.

# temps = [
#     [72, 75, 78, None, 80, 82],
#     [65, 67, "ERR", 70, 72, 74],
#     [90, 92, 91, 93, None, 95],
#     [55, 54, 56, 57, 58, "X"]
# ]

# Requirements
# Return a dictionary with:
# clean_array
# NumPy 2D float array with invalid values converted to np.nan
# city_averages
# 1D NumPy array. Mean temperature per city. Ignore NaNs.
# day_averages
# 1D NumPy array. Mean temperature per day. Ignore NaNs.
# hottest_city_index
# Index of city with highest average temperature
# coldest_city_index
# Index of city with lowest average temperature
# daily_change
# 2D NumPy array showing day-to-day temperature change per city
# Use np.diff(axis=1)
# volatility_scores
# 1D NumPy array. Standard deviation per city using np.nanstd
# extreme_days_mask
# Boolean NumPy array
# True if temperature > (city average × 1.2)
# Constraints

# Use NumPy for:
# Mean
# Std deviation
# Diff
# Masking
# Must handle: None strings No pandas Keep Python fundamentals visible
# loops for cleaning
# clear variable naming
# explicit logic
# Skills reinforced
# Data cleaning → Python + NumPy
# Axis reasoning
# Broadcasting
# Boolean masks
# Statistical intuition
# 
# Hints (only read if stuck)
# • Use np.nanmean, np.nanvar
# • For trend:
# Extract non-NaN values per row
# • np.corrcoef(clean_array) works after NaNs handled

import numpy as np

metrics = [
    [72, 75, 78, None, 80, 82],
    [65, 67, "ERR", 70, 72, 74],
    [90, 92, 91, 93, None, 95],
    [55, 54, 56, 65, 58, "X"]
]

def trend_analyzer(metrics: list[list]) -> dict:
    metric_temps:list = []
    for row in metrics:
        cleaned_temps_row:list = []
        for metric in row:
            if isinstance(metric, (int, float)) and 0 <= metric <= 120:
                cleaned_temps_row.append(metric)
            else:
                cleaned_temps_row.append(np.nan)
        metric_temps.append(cleaned_temps_row)
    metric_array = np.array(metric_temps, dtype=float)

    city_averages = np.nanmean(metric_array, axis=1)
    day_averages = np.round(np.nanmean(metric_array, axis=0), decimals=2)

    hottest_city_index = np.nanargmax(city_averages)
    coldest_city_index = np.nanargmin(city_averages)

    daily_change = np.diff(metric_array, axis=1)
    volatility_scores = np.round(np.nanstd(metric_array, axis=1), decimals=2)

    extreme_days_mask = metric_array > (city_averages[:, None] * 1.2)

    return {
        "clean_array": metric_array,
        "city_averages": city_averages,
        "day_averages": day_averages,
        "hottest_city_index": hottest_city_index,
        "coldest_city_index": coldest_city_index,
        "daily_change": daily_change,
        "volatility_scores": volatility_scores,
        "extreme_days_mask": extreme_days_mask
    }
    
def main():
    result = trend_analyzer(metrics)
    print(f"Clean Array:\n{result['clean_array']}")
    print(f"City Averages: {result['city_averages']}")
    print(f"Day Averages: {result['day_averages']}")
    print(f"Daily Change: {result['daily_change']}")
    print(f"Hottest City Index: {result['hottest_city_index']}")
    print(f"Coldests City Index: {result['coldest_city_index']}")
    print(f"Volatility Scores: {result['volatility_scores']}")
    print(f"Extreme Days Mask:\n{result['extreme_days_mask']}")

if __name__ == "__main__":
    main()

#1/14/2026 Grade 92/100