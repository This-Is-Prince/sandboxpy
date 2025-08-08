test = [2 ** x for x in range(10)]
print(test)

even_scores = [number ** 2 for number in range(10) if (number ** 2) % 2 == 0]
print(even_scores)

number_labels = ["Even" if number % 2 == 0 else "Odd" for number in range(10)]
print(number_labels)

number_labels = ["Even" if number % 2 == 0 else "Odd" for number in range(10)]
print(number_labels)

unique_squares = {x**2 for x in [-2,-1,0,1,2]}
print(unique_squares)

cubes_dict = {x: x**3 for x in range(5)}
print(cubes_dict)

large_squares_generator = (x**2 for x in range(10000000))
print(large_squares_generator)

for x in large_squares_generator:
    print(x)