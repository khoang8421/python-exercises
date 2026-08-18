# PROJECT 20 - Student Score Statistics Engine

# PROBLEM
# You are given a 2D list of student scores.
# Each inner list represents one student.
# Each student has 4 test scores.
# Some scores may be invalid.

# Your job is to clean the data, convert it to NumPy, and compute statistics.
# INPUT
# A Python list. Not NumPy yet.
# Example:

# [
# [78, 85, 90, 88],
# [92, 100, 105, 95],
# [60, 70, None, 65],
# [88, 82, 84, "A"],
# [90, 92, 94, 96]
# ]

# Rules:
# • Valid scores are integers from 0 to 100 inclusive
# • Invalid values must be removed
# • Students with fewer than 2 valid scores are excluded entirely

# REQUIRED OUTPUT
# Return a dictionary with:
# • "clean_array" A NumPy 2D array of valid scores
# • "student_averages" NumPy 1D array. One average per student "class_average" Single float. Rounded to 2 decimals
# • "top_student_index" Index of student with highest average in clean_array
# • "score_distribution" Python dict with keys: "0-59", "60-69", "70-79", "80-89", "90-100"

# Values are counts across all valid scores
# CONSTRAINTS
# You must:
# • Use NumPy for calculations
# • Use Python loops for validation
# • Use functions
# • Handle edge cases
# • No Pandas
# • No list comprehensions for cleaning
# • No hardcoded answers

# EXPECTED SKILLS USED
# • Type checking
# • Conditionals
# • Loops
# • Dict accumulation
# • NumPy arrays
# • Axis-based operations

import numpy as np

data = [
    [78, 85, 90, 88],
    [92, 100, 105, 95],
    [60, 70, None, 65],
    [88, 82, 84, "A"],
    [90, 92, 94, 96]
]

def statistics_engine(data: list[list]) -> dict:
    cleaned_data = []

    # 1. Clean the data: convert strings and None to np.nan
    for row in data:
        cleaned_row = []
        for grade in row:
            if isinstance(grade, (int, float)):
                cleaned_row.append(grade)
            else:
                cleaned_row.append(np.nan)
        cleaned_data.append(cleaned_row)

    # 2. Convert to NumPy array
    student_array = np.array(cleaned_data, dtype=float)

    # 3. Student averages (ignore NaNs)
    student_averages = np.nanmean(student_array, axis=1)

    # 4. Class average (ignore NaNs)
    class_average = round(np.nanmean(student_averages), 2)

    # 5. Top student index
    top_student_index = np.nanargmax(student_averages)

    # 6. Score distribution
    score_distribution = {
        "0-59": 0,
        "60-69": 0,
        "70-79": 0,
        "80-89": 0,
        "90-100": 0
    }

    # Flatten the array and remove NaNs
    all_scores = student_array.flatten()
    all_scores = all_scores[~np.isnan(all_scores)]

    for score in all_scores:
        if 0 <= score <= 59:
            score_distribution["0-59"] += 1
        elif 60 <= score <= 69:
            score_distribution["60-69"] += 1
        elif 70 <= score <= 79:
            score_distribution["70-79"] += 1
        elif 80 <= score <= 89:
            score_distribution["80-89"] += 1
        elif 90 <= score <= 100:
            score_distribution["90-100"] += 1

    return {
        "clean_array": student_array,
        "student_averages": student_averages,
        "class_average": class_average,
        "top_student_index": top_student_index,
        "score_distribution": score_distribution
    }

def main():
    result = statistics_engine(data)
    print("Clean Array:\n", result["clean_array"])
    print("Student Averages:", result["student_averages"])
    print("Class Average:", result["class_average"])
    print("Top Student Index:", result["top_student_index"])
    print("Score Distribution:", result["score_distribution"])

if __name__ == "__main__":
    main()