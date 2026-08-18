# Project 16 — Simple Data Normalizer

# Goal: Normalize numeric values in a dataset to the 0–1 range.

# Example Input:

# data = {"Alice": 50, "Bob": 80, "Charlie": 30}


# Example Output:

# {"Alice": 0.25, "Bob": 1.0, "Charlie": 0.0}


# Rules / Constraints:

# Use min-max normalization formula: (x - min) / (max - min)

# Handle empty data

# Round to 2 decimals

# Topics: dicts, loops, math, min/max



data = {"Alice": 50, "Bob": 80,
        "Charlie": 30, "John": 40,
        "Gerald": 65, "Antiquwa": 54,
        "Joquavious": 10}

def simple_data_normalizer(data: dict) -> dict:

    normalized_data:dict = {}
    minimum:int = None
    maximum:int = 0

    for num in data.values():
        # if not num: not excludes 0
        if num == "" or num is None:
            continue
        if num > maximum:
            maximum = num
    for num in data.values():
        if minimum is None or num < minimum:
            minimum = num
    
    if maximum == minimum:
        for key in data:
            normalized_data[key] = 0.0
    for names, num in data.items():
        normalized_data[names] = round((num - minimum) / (maximum - minimum), 2)

    return normalized_data, minimum, maximum

def main():
    normalized, min_val, max_val = simple_data_normalizer(data)
    print(normalized)
    print(min_val)
    print(max_val)

if __name__ == "__main__":
    main()

#1/1/2026 90/100
