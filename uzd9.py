name = input("izdomā vārdu ")
letter = input("izdomā burtu ")
amount = 0
for x in name:
    if x == letter:
        amount += 1
print(amount)