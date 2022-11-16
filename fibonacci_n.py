
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

fibonacci(35)
"""

def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    
    if n == 0:
        print(n1)
    elif n == 1:
        print(n2)
    else:
        while count < n:
            print(n1)
            ncount = n1 + n2
            n1 = n2
            n2 = ncount
            count += 1
        

fibonacci(1)