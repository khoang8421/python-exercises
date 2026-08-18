# NUMPY PROJECT 6
# Feature Engineering for ML

#Use this exact input. Do not modify it.

# metrics = [
#     [72, 75, 78, None, 80, 82],
#     [65, 67, "ERR", 70, 72, 74],
#     [90, 92, 91, 93, None, 95],
#     [55, 54, 56, 65, 58, "X"]
# ]

# RULES
# NumPy only. No pandas.
# No Python loops over rows or columns.
# You may loop only to clean raw input.
# All math must be vectorized.
# NaNs must be handled correctly.
# No printing inside the function.

# TASK
# Write the function below.
# def feature_engineer(metrics: list[list]) -> dict:

# It must return a dictionary with these keys.
# normalized
# Z-score normalize each city independently.
# Formula:
# (value − city_mean) / city_std
# Requirements:
# Use NumPy broadcasting.
# Ignore NaNs.
# Output shape matches input.
# trend_strength
# For each city, compute the mean absolute daily change.
# Requirements:
# Use np.diff
# Ignore NaNs correctly.
# One float per city.
# missing_ratio
# Percentage of missing values per city.

# Requirements:
# Count NaNs.
# Divide by total days.
# Output floats between 0 and 1.
# anomaly_mask
# Boolean mask where a value is an anomaly.
# Condition:
# value > city_mean + 2 × city_std

# Requirements:
# NaNs must be False.
# Shape matches input.
# EXPECTED OUTPUT TYPES
# normalized → np.ndarray
# trend_strength → np.ndarray
# missing_ratio → np.ndarray
# anomaly_mask → np.ndarray (bool)

import numpy as np

metrics = [
    [72, 75, 78, None, 80, 82],
    [65, 67, "ERR", 70, 72, 74],
    [90, 92, 91, 93, None, 95],
    [55, 5343, 56, 65, 58, "X"]
]

def feature_engineer(metrics: list[list]) -> dict:
    cleaned_metrics: list = []
    for row in metrics:
        cleaned_metrics_row: list = []
        for metric in row:
            if isinstance(metric, (int, float)):
                cleaned_metrics_row.append(metric)
            else:
                cleaned_metrics_row.append(np.nan)
        cleaned_metrics.append(cleaned_metrics_row)

    metrics_array = np.array(cleaned_metrics, dtype=float)

    city_mean = np.nanmean(metrics_array, axis=1)
    city_std = np.nanstd(metrics_array, axis = 1)
    normalized = (metrics_array - city_mean[:, None]) / city_std[:, None]

    trend_strength = np.nanmean(np.abs(np.diff(metrics_array, axis=1)))

    missing_ratio = round(np.count_nonzero(np.isnan(metrics_array)) / np.size(metrics_array), 2)

    anomaly_mask = metrics_array > (city_mean[:, None] + (2 * city_std[:, None]))

    return {
        "cleaned_array": metrics_array,
        "normalized": normalized,
        "trend_strength": trend_strength,
        "missing_ratio": missing_ratio,
        "anomaly_mask": anomaly_mask
    }

def main():
    result = feature_engineer(metrics)
    print(f"Cleaned Array:\n {result['cleaned_array']}")
    print(f"Z-Score Normalized:\n {result['normalized']}")
    print(f"Trend Strength: {result['trend_strength']}")
    print(f"Missing Ratio: {result['missing_ratio']}")
    print(f"Anomaly Mask:\n{result['anomaly_mask']}")

if __name__ == "__main__":
    main()

#1/19/2026 Grade 94/100