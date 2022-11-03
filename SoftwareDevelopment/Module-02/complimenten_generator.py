import random
BannedNumber = 1
Naam = input("wat is naam")
AantalComplimenten = int(input("getal"))
Text = ["Je bent geweldig","Je bent slim", "Je kan goed progameren", "Je bent aardig"]
for X in range(AantalComplimenten):
    RandomNumberGen = random.randint(0, 3)
    while BannedNumber == RandomNumberGen:
        RandomNumberGen = random.randint(0, 3)
    print(Text[RandomNumberGen], Naam)
    BannedNumber = RandomNumberGen
    