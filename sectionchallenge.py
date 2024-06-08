choice = "-"
while choice != "0":
    if choice in "12345":
        print("\nYou chose {}\n".format(choice))
    elif (choice < "0" or choice > "5") and choice != "-":
        print("\t*******CHOOSE A VALID OPTION!*******")
        print("\t\t\t{} is NOT valid".format(choice))

    print("Please choose your option from the list below:")
    print("1:\tLearn Python")
    print("2:\tLearn Java")
    print("3:\tGo Swimming")
    print("4:\tHave Dinner")
    print("5:\tGo to Bed")
    print("0:\tExit")
    choice = input()
else:
    print("You have exited the program. Goodbye")
