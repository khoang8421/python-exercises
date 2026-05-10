# Project 11 — Nested Structuring: Library Catalog

# Goal: Store multiple properties per key.
# Topics: Nested dictionaries, loops, accumulation.

# Prompt:
# Write a function build_library_catalog(books) where books is:

# books = [
#     {"title": "Book A", "author": "Author X", "copies": 3},
#     {"title": "Book B", "author": "Author Y", "copies": 2},
#     {"title": "Book A", "author": "Author X", "copies": 2},
# ]


# Return a dictionary mapping book titles to nested info:
# "author" → author's name
# "total_copies" → total copies across entries
# Rules / Constraints:
# Accumulate total_copies if title repeats.
# Example Input/Output:
# build_library_catalog(books)
# # Returns:
# # {
# #   "Book A": {"author": "Author X", "total_copies": 5},
# #   "Book B": {"author": "Author Y", "total_copies": 2}
# # }

books = [
    {"title": "IT", "author": "Stephen King", "copies": 312312},
    {"title": "Harry Potter", "author": "J.K Rowling", "copies": 2290382},
    {"title": "IT", "author": "Stephen King", "copies": 21234},
    {"title": None, "author": None, "copies": 0},
]


def build_library_catalog(books: list) -> dict:

    book_nested_info = {}

    for book in books:

        title: str = book["title"]
        author: str = book["author"]
        copies: int = book["copies"]

        if not title:
            continue

        if title not in book_nested_info:
            book_nested_info[title] = {
                "author": author,
                "total_copies": 0
            }
        
        book_nested_info[title]["total_copies"] += copies
    
    return book_nested_info

def main():
    print(build_library_catalog(books))

if __name__ == "__main__":
    main()

#12/28/2025 95/100