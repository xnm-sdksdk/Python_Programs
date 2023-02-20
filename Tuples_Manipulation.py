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