# Project 14 Grouping + Filtering with Dictionaries

# Goal of the code
# You will process a list of transaction records.
# You will group data by user.
# You will filter users based on risk rules.
# You will return summary statistics per user.

# This project tests whether you can combine grouping, accumulation, and filtering without forcing one pattern everywhere.

# Input
# A list of dictionaries. Each dictionary represents one transaction.

# Example input
# transactions = {
# user: "Alice", amount: 1200, type: "withdraw"
# user: "Bob", amount: 200, type: "deposit"
# user: "Alice", amount: 300, type: "withdraw"
# user: "Charlie", amount: 5000, type: "withdraw"
# user: "Bob", amount: 50, type: "withdraw"
# user: "Charlie", amount: 100, type: "deposit"
# }

# Output
# A dictionary keyed by user.
# Each user must have
# total_withdrawn
# total_deposited
# transaction_count
# flagged_user boolean

# Example output
# Alice
# total_withdrawn: 1500
# total_deposited: 0
# transaction_count: 2
# flagged_user: True

# Bob
# total_withdrawn: 50
# total_deposited: 200
# transaction_count: 2
# flagged_user: False

# Charlie
# total_withdrawn: 5000
# total_deposited: 100
# transaction_count: 2
# flagged_user: True

# Rules and constraints
# Ignore transactions with missing user or amount
# Amount is always positive when valid
# A user is flagged if total_withdrawn is greater than or equal to 1000
# Do not predefine users
# You must build the dictionary dynamically
# One pass to accumulate
# One pass to derive flags only
# Topics this uses
# Dictionary grouping by key
# Accumulating numeric values
# Filtering based on derived metrics
# Clean separation of accumulation vs derivation
# Safe dictionary initialization

transactions = [
{"user": "Alice", "amount": 1200, "type": "withdraw"},
{"user": "Bob", "amount": 200, "type": "deposit"},
{"user": "Alice", "amount": 300, "type": "withdraw"},
{"user": "Charlie", "amount": 5000, "type": "withdraw"},
{"user": "Bob", "amount": 50, "type": "withdraw"},
{"user": "Charlie", "amount": 100, "type": "deposit"},
{"user": "", "amount": 0, "type": ""}
]

def transaction_flagger(transactions: list[dict]) -> dict:

    processed_transactions: dict = {}

    for transaction in transactions:
        user: str = transaction["user"]
        amount: int = transaction["amount"]
        type:str = transaction["type"]

        if not transaction:
            continue
        if transaction is None or user == "" or amount <= 0:
            continue
            
        if user not in processed_transactions:
            processed_transactions[user] = {
                "total_withdrawn": 0.0,
                "total_deposited": 0.0,
                "transaction_count": 0,
                "flagged_user": False
            }

        if type == "withdraw":
            processed_transactions[user]["total_withdrawn"] += amount
            processed_transactions[user]["transaction_count"] += 1
            
        elif type == "deposit":
            processed_transactions[user]["total_deposited"] += amount
            processed_transactions[user]["transaction_count"] += 1

        if processed_transactions[user]["total_withdrawn"] >= 1000 and type == "withdraw":
            processed_transactions[user]["flagged_user"] = True

    return processed_transactions
    
def main():
    print(transaction_flagger(transactions))

if __name__ == "__main__":
    main()

#1/1/2026 95/100
