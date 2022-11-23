# Linear Search

# arr the array we are going to iterate over
# target param we want to find
def search(arr, target):
    for i in range(len(arr)): # iterate over the length of the array
        if arr[i] == target: # (if element in array iterartion equals target) if we found it then
            return i # return it
        
array = [2,5,8,9,10,16,22]
target = 10
print(search(array, target))