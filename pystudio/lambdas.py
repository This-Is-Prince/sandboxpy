def double(x):
    return x * 2

lambda x: x * 2

products = [('apples', 2), ('bananas', 1), ('cherries', 5)]

sorted_products = sorted(products, key=lambda item: item[1])
print(sorted_products)

multiplier = lambda x, y: x * y
print(multiplier(2,3))

printer = lambda message: print(message)
printer("This lambda is impure.")