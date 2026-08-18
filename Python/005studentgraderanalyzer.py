# Project 5 — Deriving: Student Grade Analyzer

# Goal: Compute derived stats from existing totals.
# Topics: Loops, dictionaries, math, derived properties.

# Prompt:
# Write a function analyze_grades(students) where students is:

# students = [
#     {"name": "Alice", "scores": [80, 90, 100]},
#     {"name": "Bob", "scores": [60, 70]},
# ]


# Return a dictionary mapping each student’s name to:

# "average" → average score

# "passed" → True if average ≥ 70, else False

# Rules / Constraints:

# Do not use sum() or statistics.mean().

# Handle empty score lists (average = 0, passed = False).

# Example Input/Output:

# analyze_grades(students)
# Returns:
# {
#   "Alice": {"average": 90.0, "passed": True},
#   "Bob": {"average": 65.0, "passed": False}
# }

students = [
    {"name": "Alice", "scores": [80, 90, 100]},
    {"name": "Bob", "scores": [60, 70]},
    {"name": "John", "scores": [60, 70, 66, 42, 100, 100, 72]},
    {"name": "Tommy", "scores": []},
]

def analyze_grades(students):
    
    student_grades = {}
    for student in students:
        name = student["name"]
        scores = student["scores"]

        if name not in student_grades:
                student_grades[name] = {"average": None, "passed": False}

        total = 0
        if not scores:
             continue
        else:
            for score in scores:
                total += score
            student_grades[name]["average"] = round(total / len(scores), 2)
            if student_grades[name]["average"] >= 70:
                student_grades[name]["passed"] = True

    return student_grades
    
def main():
    print(analyze_grades(students)) 

if __name__ == "__main__":
    main()

#12/28/2025 passed