

# string is the param we are going to swap
# pocket is where we are going to put the new string 
def permute(string, pocket=""): 
    if len(string) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i] # for eacher letter
            head = string[0:i] # front of the string
            tail = string[i+1:] # back of the string
            together = head + tail
            permute(together, letter + pocket)
print(permute("AB"))