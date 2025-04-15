tweet = input("Input : ")

vowel = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']

for c in tweet:
    if c in vowel:
        c = ''
    print(c, end="")
