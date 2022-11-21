import random # to use randint (random numbers)
from datetime import datetime # to get date and time
import time
import os


def read_file():
    
    if not os.path.isfile("temperature.txt"):
        print('File does not exist!')
        input()
        return
    
    
    print("\t\t Date \t   Hour\t\tTemperature")
    print()
    
    
    
    file_temp = open("temperature.txt", "r")
    listFile = file_temp.readlines() # read to a list
    file_temp.close() # close file, always necessary
    
    for line in listFile:
        fields = line.split(';')
        print("\t\t", fields[0], "\t", fields[1])
    
read_file()


