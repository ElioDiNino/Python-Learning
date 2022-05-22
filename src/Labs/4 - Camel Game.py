import random
import time
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive")
print("your desert trek and out run the natives.\n")
done = False
miles_travelled = 0
thirst = 0
camel_tiredness = 0
natives = -20
canteen_drinks = 3
oasis = random.randrange(21)
while done == False:
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")
    choice = input("Your choice? ")
    ##Choices
    if choice.upper() == "Q":
        done = True
    elif choice.upper() == "E":
        print("\nMiles travelled: ", miles_travelled)
        print("Drinks in canteen: ", canteen_drinks)
        print("The natives are", miles_travelled - natives, "miles behind you\n")
        time.sleep(1)
    elif choice.upper() == "D":
        natives += random.randrange(7,15)
        camel_tiredness = 0
        print("\nYour camel is happy and well-rested!\n")
        time.sleep(1)
    elif choice.upper() == "C":
        full_ahead = random.randrange(10,21)
        miles_travelled += full_ahead
        thirst += random.randrange(1,3)
        camel_tiredness += random.randrange(1,4)
        natives += random.randrange(7,15)
        print("\nYou travelled", full_ahead, "miles.\n")
        time.sleep(1)
    elif choice.upper() == "B":
        med_ahead = random.randrange(5,13)
        miles_travelled += med_ahead
        thirst += 1
        camel_tiredness += 1
        natives += random.randrange(7,15)
        print("\nYou travelled", med_ahead, "miles.\n")
        time.sleep(1)
    elif choice.upper() == "A":
        if canteen_drinks > 0:
            canteen_drinks -= 1
            thirst = 0
            print("\nYou are refreshed.\n")
            time.sleep(1)
        else:
            print("\nYou have no more drinks left!\n")
            time.sleep(1)
    ##Life Stats
    if thirst > 4 and thirst < 7 and done == False:
        print("You are thirsty!\n")
        time.sleep(1)
    elif thirst > 6 and done == False:
        print("You died of thirst!\n")
        done = True
    if camel_tiredness > 5 and camel_tiredness < 9 and done == False:
        print("Your camel is getting tired.\n")
        time.sleep(1)
    elif camel_tiredness > 8 and done == False:
        print("Your camel is dead.\n")
        done = True
    if natives >= miles_travelled and done == False:
        print("The natives caught up and killed you.\n")
        done = True
    elif miles_travelled - natives <= 14 and done == False:
        print("The natives are getting close!\n")
        time.sleep(1)
    if miles_travelled >= 200 and done == False:
        print("You escaped the natives!\n")
        done = True
    win = random.randrange(21)
    if oasis == win and done == False:
        canteen_drinks = 3
        thirst = 0
        camel_tiredness = 0
        print("You found an oasis!\n")
        
        
        
        
                
        
