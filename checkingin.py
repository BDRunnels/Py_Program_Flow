# 'in' is used in sequences

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("{} is NOT in {}".format(letter, parrot))
