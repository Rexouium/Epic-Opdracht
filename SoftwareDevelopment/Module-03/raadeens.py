import random
Rounds = 0
CurrentPoints = 0
StopGameSystem = ""

maxRounds = 20
while Rounds != maxRounds or StopGameSystem == "stop":
    RandomNumberGen = random.randint(0,1000)
    print(RandomNumberGen)
    wonRound = False
    LoseCount = 0
    print("Current points =", CurrentPoints)
    while LoseCount != 10 and wonRound == False:
        UserGues = int(input("Choose a number between 0 and 1000  :"))
        if UserGues == RandomNumberGen:
            CurrentPoints += 1
            wonRound = True
            Rounds += 1
            StopGameSystem = input("Stoppen? zo ja type | stop | zo niet type verder  :").lower()
        else:
            LoseCount += 1
            if RandomNumberGen > UserGues and RandomNumberGen - UserGues > 50:
                print("Raad hoger")
            elif UserGues > RandomNumberGen and UserGues - RandomNumberGen > 50:
                print("Raad lager")
            elif RandomNumberGen > UserGues and 50 > RandomNumberGen - UserGues > 20:
                print("Komt in de buurt raad hoger")
            elif UserGues > RandomNumberGen and 50 > UserGues - RandomNumberGen > 20:
                print("Komt in de buurt raad lager")
            elif RandomNumberGen > UserGues and RandomNumberGen - UserGues < 20:
                print("Zeer dichtbij gok hoger")
            elif UserGues > RandomNumberGen and UserGues - RandomNumberGen < 20:
                print("Zeer dichtbij gok lager")

if StopGameSystem == "stop":
    print("Ended with:", CurrentPoints, "points.")