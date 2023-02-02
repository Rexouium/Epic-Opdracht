import random
keepgoing = True
# items amount / active
while keepgoing:
    firstkey = False
    points = 0
    Crowbar = False

    GenRandomNumber = random.randint(1, 3)


    def zone_search(key1, pnts):
        while not key1:
            generatornumber = random.randint(1, 3)
            print(generatornumber)
            choice = int(input("1 for under the bed, 2 for in the closet, 3 for on the floor:  "))
            if choice == generatornumber:
                print("you found the key")
                key1 = True
                pnts += 1
            else:
                print("You took too long and THEY found you[ GAME OVER ]")
                pnts = 0


    def zone_search2(bar, pnts):
        while not bar:
            generatornumber = random.randint(1, 3)
            print(generatornumber)
            choice = int(input("1 for under the worktable, 2 for in the cabinet, 3 for on the table:  "))
            if choice == generatornumber:
                print("you found the crowbar")
                bar = True
                pnts += 1
            else:
                print("You took too long and THEY found you[ GAME OVER ]")
                pnts = 0


    def doorpath(key1, pnts):
        generatornumber = random.randint(1, 3)
        print(generatornumber)
        choise = int(input("1 2 or 3 (door numbers)"))
        if choise == generatornumber and key1:
            print("You opened the door to the next area")
            pnts += 1
        elif choise == generatornumber and not key1:
            print("You walk to the door but it would not open. They catch up and kill you [ Game Over ]")
            pnts = 0
        else:
            print("Wrong door quickly try again!")


    def ventpath(bar, pnts):
        generatornumber = random.randint(1, 2)
        print(generatornumber)
        choise = int(input("1 to open, 2 to wait 5 min and then open the vent:  "))
        if choise == generatornumber and bar:
            print("You opened the vent to the next area")
            pnts += 1
        elif choise == generatornumber and not bar:
            print("You walk to the door but it would not open. They catch up and kill you [ Game Over ]")
            pnts -= 1
        else:
            print("they found you and you run")


    zone_search(firstkey, points)
    while points < 20:
        GenRandomNumber = random.randint(1, 18)
        if GenRandomNumber > 0 and GenRandomNumber < 7:
            zone_search(firstkey, points)
        elif GenRandomNumber > 6 and GenRandomNumber < 13:
            doorpath(firstkey, points)
        else:
            zone_search2(Crowbar, points)
            ventpath(Crowbar, points)

    keepgoing = input("y om te veder te gaan en n om te stoppen")
    if keepgoing == "n":
        keepgoing = False
        print("the end")
    else:
        print("restart")
        keepgoing = True
