item_price = 19.99

is_game_over = False

item_number = 2

item_name = "Hey"

print("The price is:", item_price)
print("The type of item_price is:", type(item_price))

print("Is the game over?", is_game_over)
print("The type of is_game_over is:", type(is_game_over))

print("The item number is:", item_number)
print("The type of item_number is:", type(item_number))

print("The name is:", item_name)
print("The type of item_name is:", type(item_name))

project_files = ["aarambh.py", "data_boxes.py", "decision_maker.py"]

theme_color_rgb = (255, 165, 0)

print("The first file we made was:", project_files[0])

print("Original list:", project_files)
project_files[2] = "data_explorer.py"
print("Updated list:", project_files)


print("The RGB color is:", theme_color_rgb)
print("The 'Green' value is:", theme_color_rgb[1])

# theme_color_rgb[1] = 100

player_profile = {
    "username": "CodeWizard",
    "level": 5,
    "is_active": True
}

print("Player's username:", player_profile["username"])

print("Original level:", player_profile["level"])
player_profile["level"] = 6
print("New level:", player_profile["level"])

player_profile["last_seen"] = "Online now"
print("Full profile:", player_profile)

numbers_list = [1,2,2,3,4,4,4,5]

unique_numbers_set = set(numbers_list)

print("Original list with duplicates: ", numbers_list)
print("Set with only unique numbers:", unique_numbers_set)

print("Is the number 3 in our set?", 3 in unique_numbers_set)
print("Is the number 10 in our set?", 10 in unique_numbers_set)