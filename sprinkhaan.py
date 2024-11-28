import random
import sys

print("Breng Sonny de sprinkhaan naar huis.")
print("Sonny bevindt zich ergens in het gras en wil naar huis.")
print("Maak sprongen naar links en naar rechts om Sonny thuis te brengen (naar 0).")
print("Sonny heeft maar korte pootjes en kan dus maar kleine sprongetjes maken.")
print("Maar pas op voor de wind.")

zoek_Sonny = random.randint(-100, 100)   #Variabele 'zoek_Sonny' initialiseren en lees een random getal in

Sonny_is_thuis = False

while Sonny_is_thuis != True:
    try
        sprong = input(int("Geef een sprong in (max 10) en een richting (- is links en + is rechts)"))
        return sprong
        break
    except ValueError:
            print("Dat was geen getal")    #(sys.exc_info()[1])
            continue
    
    if sprong > 10: 
        sprong = 10
    elif sprong < -10:
        sprong = -10
    else:
        continue

    
    


    Sonny_is_thuis = True

print("Goed gedaan, bedankt om te spelen")


