

def binary(arr, start, end, target):
    while start <= end: # iterate from start to end
        mid = (start + end) // 2
        if arr[mid] < target: # this is to check the upper half
            start = mid + 1 # reassign our start to begin moving to the right of the array
        elif arr[mid] > target: # this is to check the lower half
            end = mid - 1 # reassign our end to begin moving to the left of the array
        else:
            return mid
        
    return start

arr = [2,5,8,10,16,22,25]

target = 10

print(binary(arr, 0, len(arr), target))