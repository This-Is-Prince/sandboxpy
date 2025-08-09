my_list = [10, 20, 30]

my_iterator = iter(my_list)
print(my_iterator)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

def countdown(n):
    print("Starting countdown!")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished!")

my_countdown = countdown(3)

print(my_countdown)

print(next(my_countdown))
print(next(my_countdown))
print(next(my_countdown))
# print(next(my_countdown))

