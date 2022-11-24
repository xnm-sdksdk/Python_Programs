
import random

chars = "abcdefghijklmnopqrstuvxyzABCDEFGHIJKLMNOPQRSTUVXYZ1234567890_-.!#$%&/()=?"

# While True this loop is going to keep running no matter what happens
while 1:
    password_length = int(input('What length you would like for your password? '))
    password_count = int(input('How many password would you like to generate? '))
    # running the loop for the count of password
    for i in range(0, password_count):
        # running the loop for the lenght of the password_length
        password = ""
        for j in range(0, password_length):
            password_character = random.choice(chars)
            print(password_character)

        





