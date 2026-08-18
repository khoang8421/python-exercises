# Project 4 — Mapping / Lookup: Country Code Translator
# Goal: Use a dictionary for fast lookups.
# Topics: Dictionaries, string handling, error handling.
# Prompt:
# Write a function translate_country(codes, code) where:

# codes is a dictionary mapping country codes to full names.
# code is a string like "US".

# Return the country name if code exists, else "Unknown code".

# Example Input/Output:
# codes = {"US": "United States", "FR": "France"}
# translate_country(codes, "FR")  # Returns: "France"
# translate_country(codes, "DE")  # Returns: "Unknown code"

codes = {"US": "United States",
         "FR": "France",
         "JA": "Japan"}

def translate_country(codes, code):
    if code in codes:
        return codes[code]
    return "Unknown code"

def main():
    print(translate_country(codes, "FR"))
    print(translate_country(codes, "US"))
    print(translate_country(codes, "JA"))
    print(translate_country(codes, ""))
    print(translate_country(codes, "SW"))

if __name__ == "__main__":
    main()

#12/28/2025 passed
