print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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
choice1=input("You are at the cross road where do you want to go? type 'left' or 'right' ").lower()
if(choice1=="right"):
  print("You fall into a hole 'Game over'")
elif(choice1=="left"):
  choice2=input("You see a lake in front of you. Do you want to 'swim' or 'wait'? ").lower()
  if(choice2=="swim"):
    print("You were attck by traut!!! 'Game over'")
  elif(choice2=="wait"):
    choice3=input("You found 3 doors of different colour? which door will you choose 'RED', 'BLUE', 'YELLOW' ").lower()
    if(choice3=="red"):
      print("You were burned by fire!!! 'Game over'")
    elif(choice3=="blue"):
      print("You were eaten by beasts!!! 'Game over'")
    elif(choice3=="yellow"):
      print("YOU WON!!!")
    else:
      print("'Game over'")