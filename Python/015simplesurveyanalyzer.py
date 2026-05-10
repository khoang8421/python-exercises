# Project 14 — Simple Survey Analyzer

# Goal: Analyze survey responses, counting frequencies of multiple-choice answers.

# Example Input:

# responses = [
#     {"age": 25, "gender": "M", "choice": "A"},
#     {"age": 30, "gender": "F", "choice": "B"},
#     {"age": 22, "gender": "M", "choice": "A"},
# ]

# Example Output:

# {"A": 2, "B": 1, "C": 0, "D": 0}


# Rules / Constraints:

# Predefined choices: A, B, C, D

# Use dicts to count frequencies

# Ignore other keys in dicts

# Topics: dicts, counting, loops

responses = [
    {"age": 25, "gender": "M", "choice": "A"},
    {"age": 30, "gender": "F", "choice": "B"},
    {"age": 29, "gender": "F", "choice": "D"},
    {"age": 24, "gender": "F", "choice": "A"},
    {"age": 22, "gender": "F", "choice": "C"},
    {"age": 24, "gender": "M", "choice": "D"},
    {"age": 20, "gender": "M", "choice": "B"},
    {"age": 20, "gender": "F", "choice": "B"},
    {"age": 22, "gender": "M", "choice": "A"},
    {"age": 21, "gender": "F", "choice": "A"},
    {"age": 22, "gender": "F", "choice": "C"},
    {"age": 22, "gender": "M", "choice": "C"},
    {"age": 23, "gender": "M", "choice": "D"},
    {"age": 24, "gender": "F", "choice": "B"},
    {"age": 24, "gender": "F", "choice": "D"},
    {"age": 26, "gender": "M", "choice": "A"},
    {"age": 28, "gender": "F", "choice": "B"},
    {"age": 22, "gender": "F", "choice": "C"},
    {"age": 25, "gender": "M", "choice": "C"},
    {"age": 24, "gender": "M", "choice": "A"},
    {"age": 21, "gender": "F", "choice": "D"}
]

def ssa(responses: list[dict]) -> dict:
    
    analyzed_responses: dict = {}

    for response in responses:

        if not response:
            continue

        choice = response["choice"]

        if choice not in analyzed_responses:
            analyzed_responses[choice] = 1
        else:
            analyzed_responses[choice] += 1

    alphabetically_ordered_responses = dict(sorted(analyzed_responses.items()))
    return alphabetically_ordered_responses

def main():
    print(ssa(responses))

if __name__ == "__main__":
    main()

#1/1/2026 90/100 quick and easy