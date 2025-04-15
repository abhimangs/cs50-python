grocery_list = {}

while True:
    try:
        item = input().upper().strip()
        if item not in grocery_list:
            # Initialize item's quantity in grocery
            grocery_list[item] = 1
        else:
            # Update item's quantity
            grocery_list[item] += 1
    except EOFError:
        sorted = dict(sorted(list(grocery_list.items())))
        for item in sorted:
            print(f"{sorted[item]} {item}")
        break
    except KeyError:
        pass
