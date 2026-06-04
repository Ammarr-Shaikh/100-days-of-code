print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')
print("Welcome to the treasure island.\n Your mission is to find the treasure.")
a =input("You are at a cross road where do you want to go?\n Type \"Left\" or \"Right\": ")
if a == "Left":
    b= input("You have come to a lake.There is an island in the middle of the lake.\n Type \"wait\" to wait for a boat. Type \"Swim\" to swim across:  ") 
    if b=="wait":
        c = input("You arrived an island unharmed. Thre is a hoouse with 3 doors.\n Which door you will pick? one red, one yellow and one blue:  ")
        if c=="Yellow":
            
            print("You win!")
        elif c == "Red":
            print("Burned by fire.\n Game over")
        elif c == "Blue":
            print("Eaten by beasts.\n Game over")
        else:
            print("Invalid input")
    elif b =="swim":
        print("Attack by trout.\nGame over")
    else:
        print("Out of context")
elif a == "Right":
    print("Fall into a hole.\nGame over")
else:
    print("Error") 