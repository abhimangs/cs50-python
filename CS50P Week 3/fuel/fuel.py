while True:
    try:
        a = input("Fraction : ")
        x , y = a.split("/")

        x = int(x)
        y = int(y)

        if y == 0 or x > y:
            raise ValueError

        fuel = round((x / y) * 100)

        if fuel <= 1:
            print("E")
            break
        elif fuel >= 99:
            print("F")
            break
        else:
            print(f"{fuel}%")
            break

    except (ValueError, ZeroDivisionError):
        pass

