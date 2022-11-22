

from math import factorial

def permutation(string):
    for j in range(factorial(len(string))):
        print("".join(string)) # joins strings
        i = len(string) - 1
        while i > 0 and string[i - 1] > string[i]:
            i -= 1
        string[i:] = reversed(string[i:]) # reversed returns a iterator object reversed
        if i > 0:
            j = i
            while string[i-1] > string[j]:
                j += 1
            temp = string[i -1]
            string[i - 1] = string[j]
            string[j] = temp
            
string= "abc"
string = list(string)
permutation(string)
        
        
        