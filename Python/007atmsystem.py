#Project 7 — Enhanced ATM Simulator with User Accounts
#Topics tested: functions, loops, conditionals, dictionaries, error handling

#Prompt:
#Write a function atm_system(users, transactions) where:
#users is a dictionary mapping username → balance.
#transactions is a list of dictionaries:
#{"user": str, "type": "deposit" or "withdraw", "amount": float}

#Apply transactions to the appropriate user.
#Withdrawals that exceed balance → skip and log "Insufficient funds for USER"

#Users not in the system → skip and log "Unknown user: USER"
#Return:
#{
#  "final_balances": {username: balance},
#  "successful": count_of_successful,
#  "failed": count_of_failed
#}

#Constraints / Skills Practiced:
#Loops, nested dicts, error handling, string formatting
#Handle empty users or empty transactions
#Avoid using sum() or other built-ins for aggregation
#Extra Challenge:
#Implement a function to return the richest user.

#EXAMPLE INPUT/OUTPUT
#atm_system(users, transactions)
#users = {
#    "Alice": 100.0,
#    "Bob": 50.0
#}

#transactions = [
#    {"user": "Alice", "type": "deposit", "amount": 25.0},
#    {"user": "Bob", "type": "withdraw", "amount": 30.0},
#    {"user": "Alice", "type": "withdraw", "amount": 200.0},
#    {"user": "Charlie", "type": "deposit", "amount": 40.0}
#]

#{
#    "final_balances": {
#        "Alice": 125.0,
#        "Bob": 20.0
#   },
#    "successful": 2,
#    "failed": 2
#}

users = {
    "Bob": 230.0,
    "Alice": 502.3,
    "James": 1203.5
}

transactions = [

    {"user": "Alice", "type": "deposit", "amount": 2500.0},
    {"user": "Bob", "type": "withdraw", "amount": 30.0},
    {"user": "Alice", "type": "withdraw", "amount": 200.0},
    {"user": "Charlie", "type": "deposit", "amount": 410.0},
    {"user": "James", "type": "deposit", "amount": 4320.0},
    {"user": "James", "type": "withdraw", "amount": 120.0},
    {"user": "Bob", "type": "withdraw", "amount": 10020.0},

]



def atm_system(users, transactions):
    successes:int = 0
    failures:int = 0
    users_copy = users.copy()

    for instance in transactions: #for each dict of the list 
        
        #establishing vars
        quantity:float = instance["amount"]
        name:str = instance["user"] 
        choice:str = instance["type"]

        #if name not in user system
        if name not in users_copy:
            failures += 1
            print(f"Unknown user: {name}")

        
        #if user is in system check choice
        elif choice == "deposit":
            users_copy[name] += quantity
            successes += 1
        
        elif choice == "withdraw":
            balance:float = users_copy[name]
            if quantity <= balance:
                users_copy[name] -= quantity
                successes += 1
            else:
                print(f"Insufficient funds for {name}.")
                failures += 1
        else:
            failures += 1

    return {
    "final_balances": users_copy,
    "successful": successes,
    "failed": failures
    }

updated_bal = atm_system(users, transactions)["final_balances"]

print(atm_system(users, transactions))

def richest_user(balances):
    if not balances:  # empty dictionary
        return None, None

    richest_name = None
    richest_balance = None

    for name, balance in balances.items():
        if richest_balance is None or balance > richest_balance:
            richest_balance = balance
            richest_name = name

    return richest_name, richest_balance
print(f"The richest user is: {richest_user(users)}.")

#12/23/2025 passed