# ASCII ART

print('\n'
      '*******************************************************************************\n'
      '          |                   |                  |                     |\n'
      ' _________|________________.=""_;=.______________|_____________________|_______\n'
      '|                   |  ,-"_,=""     `"=.|                  |\n'
      '|___________________|__"=._o`"-._        `"=.______________|___________________\n'
      '          |                `"=._o`"=._      _`"=._                     |\n'
      ' _________|_____________________:=._o "=._."_.-="\'"=.__________________|_______\n'
      '|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |\n'
      '|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". \'__|___________________\n'
      '          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |\n'
      ' _________|___________| ;`-.o`"=._; ." ` \'`."\ ` . "-._ /_______________|_______\n'
      '|                   | |o ;    `"-.o`"=._``  \'` " ,__.--o;   |\n'
      '|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________\n'
      '____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____\n'
      '/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_\n'
      '____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____\n'
      '/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_\n'
      '____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____\n'
      '/______/______/______/______/______/______/______/______/______/______/_____ /\n'
      '*******************************************************************************\n')


print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
#Backslash ignores a symbol and does not count it as code.
choice1 = input('You\'re at a crossroad, where do you want to go? '
                'Type "left" or "right".\n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. '
                    'There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat. '
                    'Type "swim" to swim across.\n').lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. "
                        "There is house with 3 doors. One red, "
                        "one yellow and one blue. "
                        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over")
        elif choice3 == "yellow":
            print("You found the treasure. You Win!")
        elif choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell in to a hole. Game Over.")
