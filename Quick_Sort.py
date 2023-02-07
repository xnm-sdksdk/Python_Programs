

def quickSort(arr, low, high):
    
    if low < high:
        
        pi = partition(arr, low, high)
        
        
        quickSort(arr, low, pi-1)
        
        quickSort(arr, pi+1, high)
        
    return arr
        
        
        
def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high-1]
    
    for j in range(low, high):
        
        if arr[j] <= pivot:
            i += 1
            arr[i].arr
    
    
    
    
    
    
    
    
    
    
    