

def selectionSort(arr):
    
    number = len(arr)
    
    for i in range(number):
        
        min = 1
        for i in range(i+1, number):
            if arr[i] < arr[min]:
                min = i
                
        arr[i], arr[min] = arr[min], arr[i]
    
    return arr