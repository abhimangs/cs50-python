#Initializing the month in a list
month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:

    date = input("Date: ")

    if "," in date and " " in date:
        date = date.replace(",", "").split(" ")

        if date[0] not in month:
            continue
        else:
            for i in range(12):
                if month[i] == date[0]:
                    MM = i + 1

        if int(date[1]) < 1 or int(date[1]) > 31:
            continue

        print(f"{date[2]}-{MM:02}-{int(date[1]):02}", end="")
        break

    elif date.count("/") == 2:
        date = date.replace(" ", "").split("/")
        if date[0] in month:
            continue
        if int(date[0]) > 12 or int(date[0]) < 1:
            continue
        if int(date[1]) > 31 or int(date[1]) < 1:
            continue

        print(f"{date[2]}-{int(date[0]):02}-{int(date[1]):02}", end="")
        break
