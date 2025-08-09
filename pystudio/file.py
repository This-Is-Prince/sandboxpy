with open("notes.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("This is the second line.\n")


with open("notes.txt", "a") as file:
    file.write("This line was appended.")

with open("notes.txt", "r") as file:
    print("Reading line by line.")
    for line in file:
        print(line.strip())