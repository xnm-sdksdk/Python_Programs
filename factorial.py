def factorial(n):
    positivo = 1
    for i in range(2, n + 1):
        positivo *= i
    return positivo
print(factorial(5))

"""
import math

def factorial(n):
    factorial = 1
    for i in range(n, 1, -1):
        factorial *= i
    print(n, factorial)
    
factorial(27)
"""
