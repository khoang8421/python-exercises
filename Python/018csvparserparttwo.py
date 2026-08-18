csv_text = """
name,age,height,BMI,gender
Alice,25,62,24.3,F
Bob,22,72,27.4,M
Kyle,18,67,21.4,M
Kaylee,20,60,24.6,F
Tiffany,15,67,26.9,F
Tim,18,66,22.2,M
"""

def csv_organizer(csv_text:str) -> dict:

    lines = csv_text.strip().split('\n')
    header = lines[0].split(',')
    organzized_data = []

    for line in lines[1:]:
        if not line.strip():
            continue

        fields = line.split(',')
        person = {}

        for i in range(len(header)):
            if i < len(fields):
                value = fields[i]
                if value.isdigit():
                    value = int(value)
                person[header[i]] = value
        organzized_data.append(person)
    return organzized_data

def main():
    print(csv_organizer(csv_text))

if __name__ == "__main__":
    main()

#1/1/2026