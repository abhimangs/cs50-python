def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Rule 1: Check length
    if len(s) < 2 or len(s) > 6:
        return False

    # Rule 2: The plate must start with at least two letters
    if not s[:2].isalpha():
        return False

    # Rule 3: The plate can only contain alphanumeric characters
    if not s.isalnum():
        return False

    # Rule 4: Numbers cannot be used in the middle of the plate
    found_number = False
    for char in s:
        if char.isdigit():
            found_number = True
        elif found_number and char.isalpha():
            return False

    # Rule 5: The plate cannot start with a zero if it contains numbers
    if any(char.isdigit() for char in s):
        first_digit_index = next((i for i, char in enumerate(s) if char.isdigit()), None)
        if first_digit_index is not None and s[first_digit_index] == '0':
            return False

    return True

main()
