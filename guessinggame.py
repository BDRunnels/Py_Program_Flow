import random

highest = 10
answer = random.randint(1, highest)
print(answer) # TODO: Remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

while guess != answer:
    guess = int(input())
    if guess == answer:
        print("Well done.")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
