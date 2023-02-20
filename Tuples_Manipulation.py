# Tuple: ordered: immutable, allows duplicate elements

print("Normal Tuple")
infotuple = ("Martin", "Madrid", 23, True) # the parentheses are optional 
print(infotuple)


# Using a function to create a Tuple from ans iterable in this case a list
print("Tuple using the tuple function from an interable")
mytuple = tuple(["Hp", "Xbox", "Logi"])
print(mytuple)


print("Accessing elements")
item = mytuple[1]
print(item)


# Iterate over a tuple
print("Iterating over Tuple")
for i in mytuple:
    print(i)


# Check if element is in Tuple
print("Check if element is in Tuple")
if "Xbox" in mytuple:
    print("Yes")
else:
    print("No")


# Return the number of elements in a tuple
print("Returning number of elements ")
chars = ("a", "b", "c", "d", "a", "e", "f", "a")
print(len(chars))


# Count elements inside a tuple
print("Counting elements")
print(chars.count("a"))


# Finding the first occurrence using Index
print("Finding the first occurrence")
print(chars.index("f"))


# Convert a list to a tuple and vice-versa
print("Convert from list to tuple")
my_list = list(chars)
print(my_list)


print("Convert from tuple to a list")
myTuple = tuple(my_list)
print(myTuple)


# Slicing
print("Slicing with Tuples")
num = (1,2,3,4,5,6,7,8,9,10,11)
ind = num[2:7]
print(ind)


# Unpacking
print("Unpacking with Tuples")
data = "Boston", "Jason Tatum", "Celtics"
city, starPlayer, team = data
print(city)
print(starPlayer)
print(team)


# Unpacking with star
print("Unpacking with star")
numbers = (0, 1, 2, 3, 4, 5, 6, 7)

a, *b , c = numbers

print(a)
print(b)
print(c)


# Return the number of bytes for optimization
print("Return the number of bytes for optimization")
import sys

myList = [0,1,2, "hello", True]

my_Tuple = (0,1,2, "hello", True)

print(sys.getsizeof(myList), "bytes")
print(sys.getsizeof(my_Tuple), "bytes")


# Compare Time between creating a list and a tuple
print("Compare Time creating a List and a Tuple")
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5,6]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5,6)", number=1000000))