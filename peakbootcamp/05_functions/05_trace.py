def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100

orders = [100, 150, 200]

for price in orders:
    amount = add_vat(price, 10)
    print(f"Price is : {price}, With VAT {amount}")