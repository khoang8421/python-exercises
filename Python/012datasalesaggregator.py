# Project 11 — Sales Data Aggregator

# Goal: Aggregate a list of sales transactions by product, computing total sales, quantity sold, and average price.

# Example Input:

# sales = [
#     {"product": "Keyboard", "price": 50, "quantity": 3},
#     {"product": "Mouse", "price": 20, "quantity": 5},
#     {"product": "Keyboard", "price": 50, "quantity": 2},
# ]


# Example Output:
# {
#     "Keyboard": {"total_sales": 250, "quantity_sold": 5, "avg_price": 50.0},
#     "Mouse": {"total_sales": 100, "quantity_sold": 5, "avg_price": 20.0}
# }

# Rules / Constraints:
# Use loops, dictionaries
# Do not use pandas
# Handle empty input
# Round average price to 2 decimals
# Topics: dicts, lists, loops, arithmetic, aggregation

sales = [
    {"product": "Keyboard", "price": 53, "quantity": 32},
    {"product": "Mouse", "price": 20, "quantity": 45},
    {"product": "Keyboard", "price": 88, "quantity": 72},
    {"product": "Keyboard", "price": 50, "quantity": 33},
    {"product": "Mouse", "price": 102, "quantity": 58},
    {"product": "Keyboard", "price": 24, "quantity": 21},
    {"product": "Keyboard", "price": 72, "quantity": 35},
    {"product": "Mouse", "price": 19, "quantity": 53},
    {"product": "Keyboard", "price": 55, "quantity": 24},
    {"product": "Keyboard", "price": 40, "quantity": 36},
    {"product": "Mouse", "price": 40, "quantity": 59},
    {"product": "Keyboard", "price": 52, "quantity": 26},
    {"product": "", "price": 0, "quantity": 0}
]

def sales_data_aggregator(sales: list[dict]) -> dict:

    sales_data: dict = {}

    if not sales:
            return {}

    for sale in sales:

        product = sale["product"]
        price = sale["price"]
        quantity = sale["quantity"]

        if product == "" or None or price == "" or None or quantity == "" or None:
            continue

        if product not in sales_data:
            sales_data[product] = {
                "total_sales": 0,
                "quantity_sold": 0,
                "avg_price": 0.0
            }
        
        sales_data[product]["total_sales"] += price * quantity
        sales_data[product]["quantity_sold"] += quantity

    for product in sales_data:
        sales_data[product]["avg_price"] = round(sales_data[product]["total_sales"] / sales_data[product]["quantity_sold"], 2)

    return sales_data


def main():
    print(sales_data_aggregator(sales))

if __name__ == '__main__':
    main()

#12/29/2025 85/100