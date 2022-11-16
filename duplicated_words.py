
str = 'Can you write code in Python? And what about JavaScript? Because I love Python and JavaScript!'

str = str.lower()

words = str.split(" ")


for i in words:
    if i == str:
        print(str, end= ' ')
