# for i in range(1, 13):
#     print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))
#     print("*" * 80)

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name))) # getting number from user
print(age)

# if age >= 18:
#     print("You are old enough to vote.")
#     print("Please put an X in the box.")
# else:
#     print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("Sorry, Yoda you die in ROTJ.")
else:
    print("You are old enough to vote.")
    print("Please put an X in the box.")
