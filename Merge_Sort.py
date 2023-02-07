

def mergeSort(arr):
    if len(arr) > 1:
        
        mid = len(arr)
        left = arr[:mid]
        
        right = arr[mid:]
        
        mergeSort(left)
        
        
        mergeSort(right)
        
        
        i = j = k = 0
        
        while i < len(left) and j < len(right):
            if left[i] == right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
            
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            j += 1
            k += 1
            
            
    return arr
            
            
            
            
            
            
            
            
            
            
            
            