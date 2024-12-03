#Grashopper - A solution
import random

position = random.randint(-100,100)
print(f"initial position: {position}")

while position not 0:
    direction = input("Provide direction (l)eft or (r)ight: ")
    print(f"direction: {direction}")
    if direction not in ["l","r"]:
        print("Goed gekozen")
    else:
        print("ongekende direction")

