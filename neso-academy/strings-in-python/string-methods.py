strip = "   Hello,      World!    "
print(strip.strip())

strip = "### Hello,    World! ##"
print(strip.strip('#'))

strip = " ### Hello,    World! ##"
print(strip.strip('#'))

print("Hello World".strip('ldoH'))

print("     Hello World!     ".lstrip())
print("     Hello World!     ".rstrip())

s = "Hello! I am Prince".rsplit()
print(s) 
# ["Hello!", "I", "am", "Prince"]