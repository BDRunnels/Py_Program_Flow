low = 1
high = 1000

print("Please think of a number between {} and {}"
      .format(low, high))

input("Press ENTER to start")

guesses = 1
while low != high:
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2
    high_low = input("My guess is {}. Should I guess higher or lower? "
                     "Enter h or l, or c if guess is correct "
                     .format(guess)).casefold()

    if high_low == "h":
        # guess higher. Low end of range becomes 1 greater than guess.
        low = guess + 1
    elif high_low == "l":
        # guess lower. High end of range comes 1 less than guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        break
    else:
        print("Please enter h, l, or c")

    guesses += 1
else:
    print("You thought of the number {}!".format(low))
    print("I got it in {} guesses".format(guesses))
