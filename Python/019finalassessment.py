# Mini Data Analysis Pipeline (FINAL ASSESSMENT)

# Goal
# You will simulate a real data workflow.

# You will:
# • Parse raw CSV text
# • Clean and validate data
# • Aggregate statistics using dictionaries
# • Normalize numeric values
# • Derive summary insights

# This mirrors real data analyst work.

# Input
# A raw CSV string.
# Example input
# csv_text = """
# name,age,score
# Alice,25,90
# Bob,22,85
# Kyle,18,100
# Kaylee,20,100
# Tiffany,15,67
# """

# Output
# A dictionary with:
# • cleaned_rows
# • average_score
# • min_score
# • max_score
# • normalized_scores

# Example output structure
# {
# "cleaned_rows": [
# {"name": "Alice", "age": 25, "score": 90},
# ...
# ],
# "average_score": 88.4,
# "min_score": 67,
# "max_score": 100,
# "normalized_scores": {
# "Alice": 0.74,
# "Bob": 0.56,
# ...
# }
# }

# Rules and constraints
# • No pandas
# • No numpy
# • No csv module
# • Use only loops, dicts, lists, math
# • Skip invalid rows
# • Convert numeric fields properly
# • Round averages and normalized values to 2 decimals
# • Min-max normalization formula
# • One pass to collect stats
# • One pass to normalize

# Topics tested
# • String parsing
# • Lists of dicts
# • Dictionary accumulation
# • Validation logic
# • Min and max tracking
# • Normalization math
# • Clean function structure
# • Separation of concerns

# If you complete this cleanly without guidance:
# You are done with Python Step 1.

# After this, we move to:
# NumPy mindset.
# Vectorized thinking.
# DataFrames.
# Real datasets.

csv_text = """
name,age,score
Alice,25,90
Bob,22,85
Kyle,18,100
Kaylee,20,100
Tiffany,15,67
John,,58
"""

def csv_parser(csv_text: str) -> dict:

    lines: str = csv_text.strip().split('\n')
    header: str = lines[0].split(',')
    organized_data = []

    for line in lines[1:]:
        if not line:
            continue
        fields = line.split(',')
        person = {}

        for i in range(len(header)):
            if i < len(fields):
                value = fields[i]
                if value.isdigit():
                    value = int(value)
                person[header[i]] = value
        organized_data.append(person)
    return organized_data
    

def score_analyzer(cleaned_data: list[dict]) -> dict:

    min_score = None
    max_score = None
    average_score = None
    total = 0
    count = 0
    
    for data in cleaned_data:
        if not data:
            continue
        score = data["score"]
        if score is None or score == "":
             continue
        total += score
        count += 1

        if score == "" or score is None:
             continue
        
        if min_score is None or score < min_score:
                min_score = score
        if max_score is None or score > max_score:
                max_score = score

    average_score = round(total / count, 2)

    def data_normalizer(cleaned_data: list[dict], min_score: int, max_score: int) -> dict:
        normalized_data = {}
        for data in cleaned_data:
            if not data:
                 continue
            score = data["score"]
            if score is None or score == "":
                 continue
            name = data["name"]
            normalized_score = round((score - min_score) / (max_score - min_score), 2)

            if name not in normalized_data:
                 normalized_data[name] = normalized_score
        
        return normalized_data

    return {
        "cleaned_rows": cleaned_data,
        "average_score": average_score,
        "min_score": min_score,
        "max_score": max_score,
        "normalized_scores": data_normalizer(cleaned_data, min_score, max_score)
        }

def main():
    cleaned_data = csv_parser(csv_text)
    analyzed_data = score_analyzer(cleaned_data)
    print(analyzed_data)
    

if __name__ == "__main__":
    main()

#1/2/2026 94/100