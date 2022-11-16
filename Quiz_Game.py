# Quiz Game

print("Welcome to the Quiz Game")


# Inicio do jogo
play = input("Do you want to play? ")

# Condição para início
if play.lower() != "yes":
    quit()

print("Okay! Let's play! :)")

# Contagem jogadas
score = 0

# Primeira questao

question = input("What does CPU stand for? ")
if question == "Central processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# segunda questao

question = input("What does GPU? ")
if question == "graphics processing unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# terceira questao

question = input("What does RAM stand for? ")
if question == "random access memory".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

# quarta questao

question = input("What does PSU stand for? ")
if question == "power supply unit".lower():
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) *100) + "%.")

input()