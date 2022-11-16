
list1 = ['Hello', 'Take']

list2 = ['Dear', 'Sir']

list3 = []

for i in list1:
    for j in list2:
        if i != j:
            res = list3.append(i+ ' ' +j)
            print(list3)


# Alternative

"""
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

res = [x + y for x in list1 for y in list2]
print(res)
"""

