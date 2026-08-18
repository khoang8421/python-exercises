# NUMPY PROJECT 4 — SENSOR DATA ANOMALY ANALYZER
# You are analyzing readings from multiple sensors over time. Data is messy. Some values are missing. Some are outliers. Your job is to clean, analyze, and flag problems using NumPy.
# You must still use Python fundamentals. Loops for cleaning. Conditionals. Dict output.

# sensor_readings = [
#     [20.5, 21.0, 20.8, None, 21.2],
#     [19.8, 20.1, "ERR", 20.0, 19.9],
#     [25.0, 80.0, 26.1, 25.8, 26.0],
#     [18.5, 18.7, 18.6, 18.4, None]
# ]

# Requirements
# Write a function:
# def sensor_analyzer(sensor_readings: list[list]) -> dict:

# Return a dictionary with:
# "clean_array"
# NumPy 2D array with invalid values converted to np.nan
# "sensor_averages"
# NumPy 1D array. Mean per sensor. Ignore NaNs
# "timepoint_averages"
# NumPy 1D array. Mean per column. Ignore NaNs
# "anomaly_mask"
# Boolean NumPy array.
# True if value > (sensor average × 1.5)
# "anomaly_counts"
# Python dict. Key = sensor index. Value = number of anomalies
# "overall_stability_score"
# Single float.
# Formula:
# 1 − (total anomalies ÷ total valid readings)
# Round to 2 decimals

# Rules
# Convert strings and None to np.nan manually
# Use np.nanmean, boolean masks, and broadcasting
# No pandas
# No try/except
# No hardcoded dimensions

# Hints (minimal)
# anomaly_mask shape must match clean_array
# Broadcasting will save you from nested loops
# Count anomalies per row using NumPy, then convert to dict

import numpy as np

sensor_readings = [
    [20.5, 21.0, 20.8, None, 21.2],
    [19.8, 20.1, "ERR", 20.0, 19.9],
    [25.0, 80.0, 26.1, 25.8, 26.0],
    [18.5, 18.7, 18.6, 18.4, None]
]

def sensor_analyzer(sensor_readings: list[list]) -> dict:
    
    cleaned_sensor_readings:list = []
    for row in sensor_readings:
        cleaned_sensor_reading_rows:list = []
        for sensor_reading in row:
            if isinstance(sensor_reading, (int, float)):
                cleaned_sensor_reading_rows.append(sensor_reading)
            else:
                cleaned_sensor_reading_rows.append(np.nan)
        cleaned_sensor_readings.append(cleaned_sensor_reading_rows)

    cleaned_sensor_array = np.array(cleaned_sensor_readings, dtype=float)
    sensor_averages = np.nanmean(cleaned_sensor_array, axis=1)
    timepoint_averages = np.nanmean(cleaned_sensor_array, axis=0)
    anomaly_mask = cleaned_sensor_array > (sensor_averages[:, None] * 1.5)
    anomaly_counts = np.sum(anomaly_mask)
    overall_stability_score = 1 - (anomaly_counts / np.count_nonzero(~np.isnan(cleaned_sensor_array)))

    return {
        "clean_array": cleaned_sensor_array,
        "sensor_averages": sensor_averages,
        "timepoint_averages": timepoint_averages,
        "anomaly_mask": anomaly_mask,
        "anomaly_counts": anomaly_counts,
        "overall_stability_score": overall_stability_score

    }

def main():
    result = sensor_analyzer(sensor_readings)
    print(f"Cleaned Array:\n{result['clean_array']}")
    print(f"Sensor Averages: {result['sensor_averages']}")
    print(f"Timepoint Averages: {result['timepoint_averages']}")
    print(f"Anomaly Mask:\n{result['anomaly_mask']}")
    print(f"Anomaly Count:\n{result['anomaly_counts']}")
    print(f"Overall Stability Score: {result['overall_stability_score']}")


if __name__ == "__main__":
    main()

#1/12/2026 92 / 100