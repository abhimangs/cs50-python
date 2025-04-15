exp = input("Expression: ")
x, y, z = exp.split(" ")
x, z = int(x), int(z)P 
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "/":
    print(f"{x / z:.1f}")
elif y == "*":
    print(f"{x * z:.1f}")
