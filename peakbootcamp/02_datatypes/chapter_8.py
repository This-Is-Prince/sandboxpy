ingredients = ["water", "milk", "black tea"]

print(f"Ingredients are: {ingredients}")

ingredients.append("sugar")

print(f"Ingredients are: {ingredients}")

ingredients.remove("water")

print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)

print(f"Chai: {chai_ingredients}")

chai_ingredients.insert(2, "black tea")

print(f"Chai: {chai_ingredients}")

last_added = chai_ingredients.pop()

print(f"{last_added}")
print(f"Chai: {chai_ingredients}")

chai_ingredients.reverse()

print(f"Chai: {chai_ingredients}")

chai_ingredients.sort()

print(f"Chai: {chai_ingredients}")

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}")
print(f"Minimum sugar level: {min(sugar_levels)}")

base_liquid = ["water", "milk"]
extra_flavour = ["ginger"]

full_liquid_mix = base_liquid + extra_flavour
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "water"] * 3
print(f"Strong brew: {strong_brew}")

# from operator import itemgetter

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}")