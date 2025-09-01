def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup

bill = calculate_bill(3, 15)

print(f"Bill is {bill}")

print("Order for table: ", calculate_bill(2, 50))