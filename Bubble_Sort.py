

def bubble(a):
    iterations = 0 # iteratorions count
    for i in range(len(a)): # iterate the array to the right
        for j in range(len(a) - i - 1): # iterate the array to the left
            iterations += 1
            if a[j] > a[j + 1]: # swaps elements if they are lower then the one on the left
                a[j], a[j + 1] = a[j + 1], a[j]
                
    return a, iterations
                
a = [9,8,7,6,5,4,3,2,1,]

print(bubble(a))