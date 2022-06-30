import random

def roll():
    dice_number = random.randint(1,6)

    if dice_number == 1:
        print("-------\n|     |\n|  *  |\n|     |\n-------")
    elif dice_number == 2:
        print("-------\n|    *|\n|     |\n|*    |\n-------")
    elif dice_number == 3:
        print("-------\n|    *|\n|  *  |\n|*    |\n-------")
    elif dice_number == 4:
        print("-------\n|*   *|\n|     |\n|*   *|\n-------")
    elif dice_number == 5:
        print("-------\n|*   *|\n|  *  |\n|*   *|\n-------")
    elif dice_number == 6:
        print("-------\n|*   *|\n|*   *|\n|*   *|\n-------")
    print(dice_number)
    
while True:
    user = input("Do you want to keep playing? (yes/no) ")

    if user == "yes":
        roll()
        
    elif user == "no":
        break
    else:
        print("Invalid option")
