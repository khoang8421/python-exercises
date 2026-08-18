# grades = [
#     [82, 91, None, 88, 75],
#     [100, 95, 98, 105, 102],
#     [70, None, 60, 72, "X"],
#     [88, 85, 90, 82, 89],
#     [55, 65, 50, 60, 58]
# ]

# Tasks:
# Clean the data: convert invalid entries (None, strings) to np.nan.
# Compute student averages: ignore np.nan.
# Compute class average: across all students and exams.
# Identify top and bottom student: by average score.
# Compute exam-wise averages: average per exam, ignoring np.nan.
# Score distribution: dictionary with grade buckets (0-59, 60-69, … 90-100).
# Optional challenge: count how many exams each student failed (<60).
# Expected Output Structure:

import numpy as np

grades = [
    [82, 91, None, 88, 75],
    [100, 95, 98, 105, 102],
    [70, None, 60, 72, "X"],
    [88, 85, 90, 82, 89],
    [55, 65, 50, 60, 58]
]

def statistics_engine(grades: list[list]) -> dict:

    cleaned_data = []
    for row in grades:
        cleaned_row = []
        for grade in row:
            if isinstance(grade, (int, float)):
                cleaned_row.append(grade)
            else:
                cleaned_row.append(np.nan)
        cleaned_data.append(cleaned_row)

    clean_array = np.array(cleaned_data, dtype=float)
    student_averages = np.nanmean(clean_array, axis=1)
    class_average = round(np.nanmean(student_averages), 2)
    top_student_index = np.nanargmax(student_averages)
    bottom_student_index = np.nanargmin(student_averages)
    exam_averages = np.nanmean(clean_array, axis=0)


    all_grades = clean_array.flatten()
    fail_count = 0
    score_distribution = {
        "0-59": 0,
        "60-69": 0,
        "70-79": 0,
        "80-89": 0,
        "90-100": 0
    }

    for grade in all_grades:
        if np.isnan(grade):
            fail_count += 1
            continue
        if 0 <= grade <= 59:
            score_distribution["0-59"] += 1
        elif 60 <= grade <= 69:
            score_distribution["60-69"] += 1
        elif 70 <= grade <= 79:
            score_distribution["70-79"] += 1
        elif 80 <= grade <= 89:
            score_distribution["80-89"] += 1
        elif 90 <= grade <= 100:
            score_distribution["90-100"] += 1

    return {
    "clean_array": clean_array,
    "student_averages": student_averages,
    "class_average": class_average,
    "top_student_index": top_student_index,
    "bottom_student_index": bottom_student_index,
    "exam_averages": exam_averages,
    "score_distribution": score_distribution,
    "fail_counts": fail_count
}
def main():
    result = statistics_engine(grades)
    print(f"Cleaned Array:\n{result['clean_array']}\n")
    print(f"Student Averages: {result['student_averages']}\n")
    print(f"Class Average: {result['class_average']}\n")
    print(f"Top Student Index: {result['top_student_index']}\n")
    print(f"Bottom Student Index: {result['bottom_student_index']}\n")
    print(f"Exam Averages: {result['exam_averages']}\n")
    print(f"Score Distribution: {result['score_distribution']}\n")
    print(f"Fail Counts: {result['fail_counts']}\n")

if __name__ == "__main__":
    main()