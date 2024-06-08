day = "Monday"
temp = 30
raining = False

if (day == "Saturday" and temp > 27) or not raining:
    print("Go swimming")
else:
    print("Learn python.")

print("-" * 80)

if 0:
    print("True")
else:
    print("False")

name = input("Enter name: ")
if name:
    print("Hello {}".format(name))
else:
    print("Are you the man with no name?")

for x in range(30):
    if x % 3 == 0 or x % 5 == 0:
        continue
    print(x)
print("-" * 80)
for x in range(30):
    if x % 3 != 0 and x % 5 != 0:
        print(x)
print("-" * 80)
for x in range(30):
    if x % 3 != 0 or x % 5 != 0:
        print(x)
