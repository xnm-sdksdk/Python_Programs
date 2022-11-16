# Jumanji

print("\n\t\n\tWelcome to Jumanji!")
name = input("\nWhat's your name player? ")
age = int(input("\nWhat's your age player? "))

print("\nHello", name, "you're ", age, "years old.")

health = 10

if age >= 18:
    print("\nYou're old enough to play, your journey is about to beggin!")


    play = str(input("\nDo you wish to beggin this aventure? ")).lower()
    if play == "yes":
        print("\nYou're starting with", health, "health")
        print("\nGood luck!")

        option = str(input("First challenge... In a trail you only have two option Left or Right, choose one: "))
        if option == "left":

            ans = str(input("Nice, you managed to reach a waterfall, do you climb ou go around it: "))
            if ans == "climb":
                print("You climbed through the waterfall, and managed to find a shelter.")

                ans = str(input("Do you choose tree or cave? "))
                if ans == "cave":
                    print("You got inside the cave and got attacked by a bear, you just lost 5 health")
                    health -= 5

                    ans = str(input("You find a sharp stick do you fight or do you run? "))
                    if ans == "fight":
                        print("You survived, congratulations. :)")
                    elif ans == "run":
                        print("Not fast enough, you just lost 5 health")
                        health -= 5
                        print("GAME OVER!!!")

                elif ans == "tree":
                    print("You climbed a tree and survived, congratulations. ")

            elif ans == "around":
                print("You chosen to go around and got attacked by a snake, you just lost 5 health")
                health -= 5

                print("You managed to find shelter")
                ans = str(input("Do you choose house or cave? "))
                if ans == "house":
                    print("You got attacked by the owner just lost 5 health.")
                    health -= 5
                    print("GAME OVER!!!")
                elif ans == "cave":
                    print("A puma just attacked you, you lost 5 health.")
                    health -= 5
                    print("GAME OVER!!!")

        elif option == "right":
            print("You managed to find a village.")

            option == str(input("Do you ask for help or continue your path? "))
            if option == "help":
                print("Now you are a prisioner. End of Game :(")
            elif option =="continue":
                print("You didn't make it through the cold and starved. End of Game :(")

    elif play == "no":
        print("Goodbye. :)")

    elif age <= 18:
        print("You're not old enough, you can't play")

input()