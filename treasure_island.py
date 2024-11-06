from random import choice

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice_1 = input('You\'r at a crossroad. Will you go left or right? '
                 'Type "left" for left and "right" for right.').lower()

if choice_1 == "left":
    choice_2 = input('You\'ve reached a lake with an island in the middle. '
          'Do you want to wait for a boat or swim across? Type "wait" to wait or "swim" to swim')
    if choice_2 == "wait":
        choice_3 = input('You arrived unharmed. Now pick a door: "blue", "yellow" or "red"').lower()
        if choice_3 == "red":
            print("It's a room full of fire... Game Over")
        elif choice_3 == "yellow":
            print("You found the treasure... Well done!")
        elif choice_3 == "blue":
            print("It's a room full of dragons... Game Over")
        else:
            print("This door doesn't exist")
    else:
        print("You got attacked by a chapri... Game Over")

else:
    print("Oh no! You were killed by the wicked witch...Game Over")


