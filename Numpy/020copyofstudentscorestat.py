import numpy as np

data = [
    [78, 85, 90, 88],
    [92, 100, 105, 95],
    [60, 70, None, 65],
    [88, 82, 84, "A"],
    [90, 92, 94, 96]
]

def statistics_engine(data):
    
    cleaned_data:list = []
    for row in data:
        cleaned_row:list = []
        for score in row:
            if isinstance(score, (int, float)):
                cleaned_row.append(score)
            else:
                cleaned_row.append(np.nan)
        cleaned_data.append(cleaned_row)
    
    student_array = np.array(cleaned_data, dtype=float)

    student_averages = np.nanmean(student_array, axis=1)

    class_average = round(np.nanmean(student_averages), 2)

    top_student_index = np.nanargmax(student_averages)

    score_distribution = {
        "0-59": 0,
        "60-69": 0,
        "70-79": 0,
        "80-89": 0,
        "90-100": 0
    }

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
    result = (statistics_engine(data))
    print("Clean Array:\n", result["clean_array"])
    print("Student Averages:", result["student_averages"])
    print("Class Average:", result["class_average"])
    print("Top Student Index:", result["top_student_index"])
    print("Score Distribution:", result["score_distribution"])

if __name__ == "__main__":
    main()