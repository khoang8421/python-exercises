#ROJECT 10
#Purchase Behavior Feature Builder
#GOAL: You will transform raw ecommerce purchase records into clean, structured user-level features.
#This mimics real feature engineering done before training ML models.

#build_user_features(purchases)

#INPUT FORMAT
#purchases
#A list of dictionaries.
#Each dictionary represents one purchase.

#Each purchase has:
#"user": string
#"product": string
#"price": float
#"quantity": int

#Example input:
# purchases = [
# {"user": "Alice", "product": "keyboard", "price": 120.0, "quantity": 1},
# {"user": "Bob", "product": "mouse", "price": 40.0, "quantity": 2},
# {"user": "Alice", "product": "keycaps", "price": 60.0, "quantity": 1}
# ]

# OUTPUT FORMAT
# Return a dictionary:
# {
# "user_features": {
# user_name: {
# "total_spent": float,
# "total_items": int,
# "avg_item_price": float,
# "unique_products": int,
# "high_value_user": bool
# }
# },
# "top_spender": str or None
# }

# Example output for the input above:

# {
# "user_features": {
# "Alice": {
# "total_spent": 180.0,
# "total_items": 2,
# "avg_item_price": 90.0,
# "unique_products": 2,
# "high_value_user": False
# },
# "Bob": {
# "total_spent": 80.0,
# "total_items": 2,
# "avg_item_price": 40.0,
# "unique_products": 1,
# "high_value_user": False
# }
# },
# "top_spender": "Alice"
# }

# RULES AND CONSTRAINTS
# All users start with zero totals
# total_spent = sum(price × quantity)
# avg_item_price = total_spent / total_items
# high_value_user = total_spent ≥ 500
# If total_items is 0 → avg_item_price = 0.0

# Invalid records must be ignored:
# Missing keys
# Wrong data types
# Negative or zero price
# Negative quantity

# Do not mutate the input list
# No global variables
# No pandas, numpy, collections, or sorting
# Use loops and dictionaries only

# EDGE CASES
# Empty purchase list
# Single-user dataset
# Same product bought multiple times

# Ties for top_spender
# Return the user who reached that amount first
# Records with zero quantity

purchases = [
    {"user": "Alice", "product": "keyboard", "price": 120.0, "quantity": 1},
    {"user": "Bob", "product": "mouse", "price": 40.0, "quantity": 2},
    {"user": "Alice", "product": "keycaps", "price": 60.0, "quantity": 1}
]

# total_spent = sum(price × quantity)
# avg_item_price = total_spent / total_items
# high_value_user = total_spent ≥ 500
# If total_items is 0 → avg_item_price = 0.0

def build_user_features(purchases):

    user_features = {}
    top_spender = None
    max_spent = 0.0

    for purchase in purchases:
        user = purchase["user"]
        product = purchase["product"]
        price = purchase["price"]
        quantity = purchase["quantity"]


        if user not in user_features:
            user_features[user] = { #default values told to be made 0/None
                "total_spent": 0.0,
                "total_items": 0,
                "products": set(),
                "avg_item_price": 0.0,
                "unique_products": 0,
                "high_value_user": False
            }
        
        total_spent = price * quantity
        total_item = quantity

        #Previously, I had assumed that if Alice was stored, the next time we see Alice wouldn't be stored because it was already stored by the first dict.
        #However, this isn't the case becuase dict 1 being purchases["Alice"] is the same as dict 3 being purchases["Alice"]
        #All I need to do is to use the += instead of assigning it as = each time.
        user_features[user]["total_spent"] += total_spent
        user_features[user]["total_items"] += total_item
        user_features[user]["products"].add(product)

    for user, data in user_features.items():
        user_features[user]["unique_products"] = len(data["products"])
        user_features[user]["avg_item_price"] = user_features[user]["total_spent"] / user_features[user]["total_items"]
        user_features[user]["high_value_user"] = user_features[user]["total_spent"] >= 500

        if user_features[user]["total_spent"] > max_spent:
            top_spender = user
        
        del user_features[user]["products"]

    return {
        "user_features": user_features,
        "top_spender": top_spender
    }

def main():
    print(build_user_features(purchases))
    
if __name__ == "__main__":
    main()

#12/27/2025
# Failed like 67% in, needed CHATGPT