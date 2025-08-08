def change_number(n):
    n = 100
    print(f"Inside function, n is: {n}")

my_number = 5
change_number(my_number)
print(f"Outside function, my_number is still: {my_number}")

def add_to_my_list(items):
    items.append("NEW")
    print(f"Inside function, list is: {items}")

my_list = ["A", "B"]
add_to_my_list(my_list)
print(f"Outside function, list has been changed: {my_list}")

