name = input("camelCase: ")

for c in name:
    if c.isupper():
        print("_", end="")
        c = c.lower()
    print(c, end="")
