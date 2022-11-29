import random
AantalVragenGestelt = 0
GoedeAntwoorden = 0
LVL = 0
Randomiser = random.randint(0, 999)
while LVL != 20:
    while AantalVragenGestelt < 10:
        GebruikerAntWoord = int(input("Getal tusstn 0 en 1000"))
        if Randomiser > GebruikerAntWoord and Randomiser - GebruikerAntWoord > 50:
            print("Raad hoger")
            AantalVragenGestelt += 1
        elif GebruikerAntWoord > Randomiser and GebruikerAntWoord - Randomiser > 50:
           print("Raad minder")
           AantalVragenGestelt += 1
        elif Randomiser > GebruikerAntWoord and 50 > Randomiser - GebruikerAntWoord > 20:
           print("In de buurt raad hoger")
           AantalVragenGestelt += 1
        elif GebruikerAntWoord > Randomiser and 50 > GebruikerAntWoord - Randomiser > 20:
            print("In de buurt raad minder")
            AantalVragenGestelt += 1
        elif Randomiser > GebruikerAntWoord and Randomiser - GebruikerAntWoord < 20:
            print("Heel erg in de buurt raad hoger")
            AantalVragenGestelt += 1
        elif GebruikerAntWoord > Randomiser and GebruikerAntWoord - Randomiser < 20:
            print("Getting very warm, guess lower.")
            AantalVragenGestelt += 1
        else:
            print("Juiste Antwoord gegeven goed gedaan")
            GoedeAntwoorden += 1
            LVL += 1
            AantalVragenGestelt = 0
            Stoppen = input("Stoppen of niet?").lower()
            if Stoppen == "stoppen":
                print("Stopping the game")
                raise NameError("Spel gestopt")