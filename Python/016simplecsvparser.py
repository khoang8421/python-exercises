# Project 15 — Simple CSV Parser

# Goal: Parse a CSV string into a list of dictionaries.

# Example Input:

# csv_text = "name,age,score\nAlice,25,90\nBob,22,85"


# Example Output:

# [
#   {"name": "Alice", "age": "25", "score": "90"},
#   {"name": "Bob", "age": "22", "score": "85"}
# ]


# Rules / Constraints:
# Do not use pandas or csv module
# Handle arbitrary number of rows/columns
# Return a list of dicts
# Topics: strings, lists, dicts, parsing, loops

csv_text = """
name,age,score
Alice,25,90
Bob,22,85
Kyle,18,100
Kaylee,20,100
Tiffany,15,67
"""

def csv_parser(csv_text: str) -> list[dict]:

    lines = csv_text.strip().split("\n") #stripping fo whitespace and creating substrings for every new line.
    list_of_people:list = []
    
    header = lines[0].split(',') #the header is assumed to be the first line which is split by commas
    for line in lines[1:]: #for each line in lines but excluding the first line which is header
        if not line.strip():
            continue

        fields = line.split(',') #split the individual fields by comma like we did to the header
        person = {} #create our individual dict for each person

        for i in range(len(header)): #for i in range of the amount of categories in the header which is 3
            if i < len(fields): 
                value = fields[i]
                if value.isdigit():
                    value = int(value)
                person[header[i]] = value  #stores each splitted field and stores it into the person dictionary

        list_of_people.append(person) #append each individual dict to the final list
    return list_of_people

def main():
    print(csv_parser(csv_text))

if __name__ == "__main__":
    main()

#1/1/2026 Grade: 90/100