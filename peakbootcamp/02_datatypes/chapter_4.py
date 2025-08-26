is_boiling = True
stir_count = 5

total_actions = stir_count + is_boiling # up casting
print(f"Total actions: {total_actions}")

milk_resent = 0 
print(f"Is there milk? {bool(milk_resent)}")

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")