# Lists: ordered, mutable, and allows duplicate elements


carList = ["Ferrari", "Porsche", "Aston Martin"]
print(carList)


# Create an empty List
print("Empty List")
myList = list()
print(myList)


# Different Data Types
dataTypes = [21, True, "HP"]
print(dataTypes)


# Accessing elements
print("Accessing Elements")
items = carList[0]
print(items)


# Iterate over the list
print("Iteration")
for i in carList:
    print(i)


# Check if item in List
if "Aston Martin" in carList:
    print("Yes")
else:
    print("No")


# Check how many elements
print("Checking how many elements inside")
print(len(carList))


# Append elements to the List
print("Append")
carList.append("Jaguar")
print(carList)


# Insert Element into certain position
carList.insert(1, "Mercedes-Benz")
print(carList)


# Removes Item using Pop and returns it
print("Pop")
car = carList.pop()
print(car)
print(carList)


# Remove a specific element using Remove
elem = carList.remove("Ferrari")
print(carList)


# Reverse the List using Reverse method
print("Reverse")
rev = carList.reverse()
print(carList)


# Sort the list using Sort method
print("Sort")
sort = carList.sort()
print(carList)


# Sorted organizes the list including negative numbers
# Sort places the negative numbers at the end of the list
print("Sorted")
numbers = [1,2,3,5-1,10,-3]
num = sorted(numbers)
print(numbers)

sort = numbers.sort()
print(numbers)


# Create a list containing the same element multiple times
print("List Multiplication")
multi = [0] * 5
print(multi)


# Concatenate Two Lists
print("Concatenate Two Lists")
new_multi = [1,2,3,4,5]
concatenate = multi + new_multi
print(concatenate)


# Slicing access sub parts of the List
print("Slicing")
sliceList = [1,2,3,4,5,6,7,8,9,10]
cut = sliceList[1:5]
print(cut) 


# Stepping over List Elements
print("Stepping")
step = sliceList[::2]
print(step)


# Copying a List
print("Copy")
pc = ["HP", "Asus", "Apple"]
copy = pc
copy.append("Huawei")
print(copy)

print("Copy using method")
copy = pc.copy()
print(copy)

print("List Function")
listFunction = list(pc)
print(listFunction)

# Using Slicing
print("Using Slicing")
copy = pc[:]
print(copy)
print(pc)


# List Comprehension
print("List Comprehension")
a = [1,2,3,4,5]
b = [i*i for i in a]
print(b)





