import random

#variables

Rounds = 0
Score = 0
antwoord = ""
NewRound = ""

Gueses = 10
UserGues = ""

while Gueses != 0:
    RandomNumberGen = random.randint(1, 1000)
    print(RandomNumberGen)
    while not ((UserGues := input("Say, Stop to stop or gues a number between 1 and 1000")).isdigit() and 1 < int(UserGues) < 1000):
        if UserGues.lower() == "stop":
            exit(f"Your score was: {Score} in round {Rounds}")
        print("We said to choose a number between 1 to 1000 or stop, friend")

    UserGues = int(UserGues)

    if UserGues == RandomNumberGen:
        Gueses = 0
        Rounds += 1
        Score += 1
    else:
        Gueses -= 1

        if RandomNumberGen > UserGues and RandomNumberGen - UserGues > 50:
            print("Raad hoger")
        elif UserGues > RandomNumberGen and UserGues - RandomNumberGen > 50:
            print("Raad lager")
        elif RandomNumberGen > UserGues and 50 > RandomNumberGen - UserGues > 20:
            print("Komt in de buurt raad hoger")
        elif UserGues > RandomNumberGen and 50 > UserGues - RandomNumberGen > 20:
            print("Komt in de buurt raad hoger")
        elif RandomNumberGen > UserGues and RandomNumberGen - UserGues < 20:
            print("Zeer dichtbij gok hoger")
        elif UserGues > RandomNumberGen and UserGues - RandomNumberGen < 20:
            print("Zeer dichtbij gok lager")