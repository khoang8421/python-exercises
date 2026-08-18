# Project 13 Context-Aware Word Frequency Analyzer

# Goal of the code
# You will analyze text and return the top N most frequent words after applying multiple constraints.

# This forces you to combine
# preprocessing, filtering, accumulation, derivation, sorting logic using dicts

# Input
# text string
# top_n integer
# min_length integer

# Example Input
# text = "I love Python. Python is great. I love coding every single day."
# top_n = 3
# min_length = 4

# Expected Output
# {"python": 2, "love": 2, "coding": 1}

# Explanation
# Case-insensitive
# Punctuation removed
# Words shorter than min_length ignored

# Only top N words returned
# If counts tie, keep the word that appears first in the text
# Rules and constraints
# Case-insensitive
# Ignore punctuation
# Ignore words shorter than min_length
# Ignore empty strings
# Do NOT use Counter
# Do NOT sort the entire dictionary directly
# You must manually determine top N using logic
# One dict for counts
# One dict for final result
# Topics this uses
# Text normalization
# Conditional filtering before accumulation
# Dictionary accumulation
# Tie-breaking logic
# Deriving a subset from a dict
# Avoiding over-reliance on sorting

# Hints you are allowed to use
# You may store first-seen index for tie-breaking
# You may loop multiple times
# You may track max values manually

text = """A paragraph in a book serves as a building block for ideas,
setting tone, introducing characters, or developing developing developing developing plot, with length
varying greatly from short, punchy exchanges to longer descriptive passages,
but generally aiming for unity where sentences support a single thought, often
using an introduction, supporting details, and a concluding concluding sentence to
transition or summarize, and while some recommend 100-200 words, modern
digital trends favor shorter paragraphs, all depending on the authors'
'purpose, genre, and desired reader engagement engagement engagement.
"""

import string

def text_analyzer(text: str, number_of_top_words: int, min_length_of_word:int) -> dict:
    cleaned_up_words: list = []
    counted_words: dict = {}
    words_of_min_length: dict = {}
    top_words: dict = {}


    for word in text.split():

        if not word:
            continue

        word = word.lower().translate(str.maketrans('', '', string.punctuation))
        cleaned_up_words.append(word)

        if not word:
            continue
        
    i:int = 0
    while i < len(cleaned_up_words):
        if cleaned_up_words[i] not in counted_words: counted_words[cleaned_up_words[i]] = 1
        else: counted_words[cleaned_up_words[i]] += 1
        i+=1

    for word in cleaned_up_words:
        if len(word) >= min_length_of_word:
            words_of_min_length[word] = counted_words[word]
    
    def top_n(n):
        i = 0
        while i < n:
            top_word = None
            top_count = -1
            for word, count in words_of_min_length.items():
                if count >= top_count:
                    top_word = word
                    top_count = count
            top_words[top_word] = top_count
            del words_of_min_length[top_word]
            i += 1

            if top_word is None:
                break

    top_n(number_of_top_words) 

    return {"counted_words": counted_words,
            "top_words": top_words}
    
        
def main():
    print(text_analyzer(text, 3, 4))

if __name__ == "__main__":
    main()

#12/30/2025 87 / 100