# PROJECT N1-R — NumPy Reinforcement: Performance Analyzer
# NumPy Reinforcement 2

# Goal of the code
# Analyze student performance using NumPy.
# You must clean mixed data, compute statistics, and derive insights using array logic.

# Input
# A Python list of lists. Each inner list represents one student’s exam scores.
# scores = [
#     [85, 90, 88, None, 92],
#     [70, 75, "X", 80, 78],
#     [95, 100, 98, 97, 96],
#     [60, None, 65, 62, 58],
#     [88, 84, 86, 90, 89]
# ]
# Required Output
# Return a dictionary with the following keys.
# • "clean_array" 2D NumPy array with invalid values replaced by np.nan
# • "student_averages" 1D NumPy array of each student’s average. Ignore NaNs.
# • "exam_averages" 1D NumPy array. Average score per exam column.
# • "pass_counts" 1D NumPy array. Number of scores ≥ 70 per student.
# • "top_student_index" Index of the student with the highest average.
# • "bottom_student_index" Index of the student with the lowest average.
# • "overall_pass_rate" # Single float. # (total scores ≥ 70) / (total valid scores) # Rounded to 2 decimals.

# Rules / Constraints
# • Use NumPy for all numeric computation
# • Use Python only for cleaning and looping
# • Ignore invalid values safely
# • No hardcoded dimensions
# • One clean pass for cleaning
# • No nested NumPy loops

# Topics this uses

# • np.array
# • np.nan
# • np.nanmean
# • Boolean masking
# • axis logic
# • Aggregation
# • Index derivation
# • Python + NumPy integration

import numpy as np

scores = [
    [85, 90, 88, None, 92],
    [70, 75, "X", 80, 78],
    [95, 100, 98, 97, 96],
    [60, None, 65, 62, 58],
    [88, 84, 86, 90, 89]
]

def performance_analyzer(scores):

    cleaned_data:list = [] 
    for row in scores:
        cleaned_row:list = []
        for score in row:
            if isinstance(score, (int, float)):
                cleaned_row.append(score)
            else:
                cleaned_row.append(np.nan)
        cleaned_data.append(cleaned_row)

    cleaned_array = np.array(cleaned_data, dtype=float)

    #student averages

    student_averages = np.nanmean(cleaned_array, axis=1)

    #exam averages

    exam_averages = np.nanmean(cleaned_array, axis=0)

    #pass_counts
    pass_counts: int = 0
    total_counts: int = 0
    all_scores = cleaned_array.flatten()
    for score in all_scores:
        if np.isnan(score):
            total_counts += 1
            continue
        elif score >= 70:
            pass_counts += 1
            total_counts += 1

    #top and bottom student index
    top_student_index:int = np.nanargmax(student_averages)
    bottom_student_index:int = np.nanargmin(student_averages)

    #overall pass rate
    valid_mask = ~np.isnan(cleaned_array)
    pass_mask = cleaned_array >= 70
    print(valid_mask)
    print(pass_mask)
    overall_pass_rate = round(np.sum(pass_mask) / np.sum(valid_mask), 2)


    return {
        "clean_array": cleaned_array,
        "student_averages": student_averages,
        "exam_averages": exam_averages,
        "pass_counts": pass_counts,
        "top_student_index": top_student_index,
        "bottom_student_index": bottom_student_index,
        "overall_pass_rate": overall_pass_rate
    }

def main():
    result = performance_analyzer(scores)
    print(f"Cleaned Array:\n{result['clean_array']}")
    print(f"Student Averages: {result['student_averages']}")
    print(f"Exam Averages: {result['exam_averages']}")
    print(f"Pass Counts: {result['pass_counts']}")
    print(f"Top Student Index: {result['top_student_index']}")
    print(f"Bottom Student Index: {result['bottom_student_index']}")
    print(f"Overall Pass Rate: {result['overall_pass_rate']}")

if __name__ == "__main__":
    main()

# 1/8/2026