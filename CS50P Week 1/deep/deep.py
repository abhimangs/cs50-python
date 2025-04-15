string = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
string = string.strip().lower()
if string in ["42", "forty two", "forty-two"]:
    print("Yes")
else:
    print("No")
