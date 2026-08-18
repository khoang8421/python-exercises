# Project 6 — Accumulating: Word Frequency Counter
# Goal: Build a dictionary to count occurrences of each word in a text.
# Topics: Loops, conditionals, dictionaries, string handling.

# Prompt:
# Write a function word_counter(text) that:
# Counts how many times each word appears in the string text.

# Returns a dictionary mapping words to counts.
# Rules / Constraints:
# Case-insensitive ("Apple" and "apple" count as same).

# Ignore punctuation.
# Do not use collections.Counter.
# Example Input/Output:
# text = "Apple apple banana!"
# word_counter(text)
# # Returns: {'apple': 2, 'banana': 1}

text = """My husband, he tried to speak up about what was happening,” Terry says. “When he stumbled on what he thought was causing all the cancer in town, they did everything to destroy us.

Destroy us. State-wide lying and deceit. Play your cards close. Her words sound a little dramatic, maybe paranoid. I had come to her for genealogy, and here she was diverting the entire thread.

"""

import string

def word_counter(text: str) -> dict:
    word_count_dict: dict = {}

    if not text:
        word_count_dict["Word"] = None
    else:
        list_of_text: list = text.split()
        i = 0
        # Step 1: clean up the text
        while i < len(list_of_text):
            list_of_text[i] = list_of_text[i].lower().translate(str.maketrans('', '', string.punctuation))
            i += 1

        for word in list_of_text:
            if word not in word_count_dict:
                word_count_dict[word] = 1
            else:
                word_count_dict[word] += 1

        return word_count_dict
    
def main():
    # print(word_counter(text))
    print(word_counter(text))
    
if __name__ == "__main__":
    main()

#12/28/2025 passed