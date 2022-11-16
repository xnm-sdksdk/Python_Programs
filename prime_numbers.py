# from hack in science


def is_prime(n):
    if n==2 or n==3:
        return True
    if n%2==0 or n<2:
        return False
    for i in range(3,int(n**0.5)+1,2):   
        if n%i==0:
            return False   
    return True

"""
def is_prime(n):                               
    if n <= 1:                                 
        return False                           

    for number in range(2, int(n ** 0.5) + 1):  
        if n % number == 0:                    
            return False                       

    return True       
"""