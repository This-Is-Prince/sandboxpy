try:
    with open("data.txt", "w+") as f:
        f.write("Hello World")

        print(f"Position after writing: {f.tell()}")

        f.seek(0)
        print(f"Position after seeking to start: {f.tell()}")

        content = f.read()
        print(f"Content read from file: {content}")

except Exception as e:
    print(f"There is an error {e}")

print()

try:
    with open("data.txt", "r", encoding="utf-8") as f:
        content = f.read()
        print(content)
except Exception as e:
    print(f"There is an error {e}")