my_list = [10, 20, 30]
my_tuple = ('a', 'b', 'c')
my_set = {100, 200, 300}

print("Is 20 in my_list?", 20 in my_list)
print("Is 'd' in my_tuple?", 'd' in my_list)
print("Is 400 in my_set?", 400 in my_set)

print("Is 'py' in 'python'?", 'py' in 'python')

player_profile = {"username": "CodeWizard", "level": 6}
print("Is 'level' a key in player_profile?", 'level' in player_profile)
print("Is 'CodeWizard' a key in player_profile?", 'CodeWizard' in player_profile)

empty_dict = {}
empty_set = set()

print(type(empty_dict))
print(type(empty_set))

my_set = {10,20,30}
my_dict = {"a": 1, "b": 2}

list_from_set = list(my_set)
print("List from set:", list_from_set)

tuple_from_set = tuple(my_set)
print("Tuple from set:", tuple_from_set)

list_from_dict = list(my_dict)
print("List from dict (keys):", list_from_dict)

tuple_from_dict = tuple(my_dict)
print("Tuple from dict (keys):", tuple_from_dict)

list_of_pairs = [('username', 'CodeWizard'), ('level', 7)]

dict_from_list = dict(list_of_pairs)
print("Dict from a list of pairs:", dict_from_list)

tuple_of_pairs = (('username', 'CodeWizard'), ('level', 7))

dict_from_tuple = dict(tuple_of_pairs)
print("Dict from a tuple of pairs:", dict_from_tuple)