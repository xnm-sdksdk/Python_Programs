import string

x = string.ascii_lowercase

y = list(x)

for i in y:
    for j in y:
        if i != j:
            print(i + j)
        