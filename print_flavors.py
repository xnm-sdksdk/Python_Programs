FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

for i in FLAVORS:
    for j in FLAVORS:
        if i != j:
            print(i + ", " + j)
        elif i == i:
            break
        elif j == j:
            break
        else:
            continue