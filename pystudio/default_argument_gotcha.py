def add_item_to_list(item, target=[]):
    target.append(item)
    return target

my_list_1 = add_item_to_list(1)
print(my_list_1)

my_list_2 = add_item_to_list(2)
print(my_list_2)

my_list_3 = add_item_to_list(3)
print(my_list_3)

def add_item_to_list_safe(item, target=None):
    if target is None:
        target = []

    target.append(item)
    return target

print()

my_list_1 = add_item_to_list_safe(1)
print(my_list_1)

my_list_2 = add_item_to_list_safe(2)
print(my_list_2)

my_list_3 = add_item_to_list_safe(3)
print(my_list_3)