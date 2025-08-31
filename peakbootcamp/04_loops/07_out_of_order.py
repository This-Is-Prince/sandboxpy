flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    elif flavour == "Discontinued":
        break
    else:
        print(f"Flavour is {flavour}")