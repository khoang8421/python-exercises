# Personal Finance Tracker CLI

A lightweight command-line Python application that processes bank transaction data from a CSV file, categorizes expenses, and generates monthly financial summaries.

This project was built using only Python’s standard library (`csv` and `json`) to strengthen my fundamentals in file handling, data processing, and program design.

---

## Features

- Reads transaction data from CSV files
- Automatically categorizes expenses (e.g., Food, Transport, Entertainment, Utilities)
- Calculates monthly spending summaries
- Outputs clean financial reports
- Exports structured data using JSON
- Fully built with Python standard library (no external dependencies)

---

## Example Input (CSV)

```csv
date,description,amount
2026-01-01,Starbucks,-5.75
2026-01-03,Uber,-12.30
2026-01-05,Salary,2500.00
```

---

## Example Output

```
Monthly Summary - January 2026
--------------------------------
Income:        $2500.00
Expenses:      $450.32
Net Savings:   $2049.68

Top Categories:
- Food: $120.50
- Transport: $85.20
- Utilities: $60.00
```

---

## Project Structure

```bash
personal-finance-tracker-cli/
│
├── src/
│   ├── main.py            # Entry point of the program
│   ├── parser.py          # Handles CSV reading and parsing
│   ├── categorizer.py     # Classifies transactions into categories
│   └── report.py          # Generates summary reports
│
├── data/
│   └── sample_transactions.csv
│
├── output/
│   └── monthly_report.txt
│
├── README.md
├── LICENSE
└── .gitignore
```

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/khoang8421/personal-finance-tracker-cli.git
cd personal-finance-tracker-cli
```

Run the program:

```bash
python src/main.py
```

---

## What I Learned

Through this project, I improved my understanding of:

- File I/O in Python
- Working with CSV and JSON data
- Structuring multi-file Python programs
- Data aggregation and transformation
- Designing clean CLI workflows

---

## Future Improvements

- Add support for multiple bank formats
- Improve categorization using keyword mapping or ML
- Add data visualization (charts)
- Export to Excel or PDF reports
- Build a simple GUI version

---

## License

This project is licensed under the MIT License.
