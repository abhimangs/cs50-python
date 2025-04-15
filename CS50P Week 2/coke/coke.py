total_due = 50
accepted_coins = [25, 10, 5]

while total_due > 0:
    coin = int(input("Insert Coin: "))

    if coin in accepted_coins:
        total_due -= coin

        if total_due > 0:
            print(f"Amount Due: {total_due}")
        elif total_due == 0:
            print("Change Owed: 0")
        elif total_due < 0:
            change = abs(total_due)
            print(f"Change Owed: {change}")

    else:
        print(f"Amount Due: {total_due}")
