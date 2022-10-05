from random import randint

Start_Game = input("Want to start? J/N").upper()
if Start_Game == "N":
       raise NameError("User Closed the game,")
    
elif Start_Game == "J":
    print("Its dark outside you see trough a small crack in the wall,")
    print("You look around and see a door with a keylock on it")
    Current_Room = 0

while Current_Room == 0:
    print("find the key")
    search_Key = input("Choose to search the: shelve, bed, closet")
    if search_Key == "shelve":
        print("Key found")
        access_to_rooms = True
        Current_Room += 1
    else:
        print("You found nothing usefull")
    
if access_to_rooms == True:
    while Current_Room <10:
        RightDoor = randint(1, 3)
        print("Rightdoor =", RightDoor)
        ChosenDoor = int(input("Choose a door 1 2 or 3"))
        if ChosenDoor == RightDoor:
            Hide_Randomiser = randint(0,1)
            if Hide_Randomiser == 1:
                Hide_Promt = input("Hide? J/N")
                if Hide_Promt == "N":
                    print("You died")
                    break
                elif Hide_Promt == "J":
                    Current_Room += 1
                    print("Entering next room")
                    print("Current room number",Current_Room)
            elif Hide_Randomiser == 0:
                Current_Room += 1
                print("Current room:", Current_Room)
        elif ChosenDoor != RightDoor:
            print("You died")
            break

if Current_Room == 10:
            print("You win")