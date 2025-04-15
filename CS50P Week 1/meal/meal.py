def main():
    time = input("What time is it? ")
    num = convert(time)

    if 7 <= num <= 8:
        print("breakfast time")
    if 12 <= num <= 13:
        print("lunch time")
    if 18 <= num <= 19:
        print("dinner time")


def convert(time):
    hour, mins = time.split(":")
    return int(hour) + int(mins) / 60


if __name__ == "__main__":
    main()
