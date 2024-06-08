shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# for item in shopping_list:
#     if item != "spam":
#         print("Buy {}".format(item.upper()))

for item in shopping_list:
    if item == "spam":
        continue
    print("Buy {}".format(item))

item_to_find = "spam"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
# EASIER WAY TO WRITE ABOVE
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("{} found at position {}".format(item_to_find, found_at))
else:
    print("{} not found".format(item_to_find))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1
