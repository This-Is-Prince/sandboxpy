my_data = [("user_a", {"email", "login"}), ("user_b", {"login"})]

print("Original data:", my_data)

my_data[0][1].add("admin_access")
print()

print("Modified data:", my_data)