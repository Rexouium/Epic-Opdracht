from random import randint

StartGame = input("Want to start? J/N").upper()
if StartGame == "N":
       raise NameError("User Closed the game,")
    
elif StartGame == "J":
    print("Its dark outside you see trough a small crack in the wall,")
    print("You look around and see a door with a keylock on it")
    CurrentRoom = 0

else:
    raise NameError("Wrong input")

while CurrentRoom == 0:
    print("find the key")
    searchKey = input("Choose to search the: shelve, bed, closet")
    if searchKey == "shelve":
        print("Key found")
        TakenKeyBack = input("Will you take the key with you? J/N")
        CurrentRoom = 1
    else:
        print("You found nothing usefull")

while CurrentRoom <10:
    RightDoor = randint(1, 3)
    print("Rightdoor =", RightDoor)
    Chosen_Door = int(input("Choose a door 1 2 or 3"))
    if Chosen_Door == RightDoor:
        HideRandomiser = randint(0,1)
        if HideRandomiser == 1:
            HidePromt = input("Hide? J/N")
            if HidePromt == "N":
                print("You died")
                break
            elif HidePromt == "J":
                CurrentRoom += 1
                print("Entering next room")
                print("Current room number",CurrentRoom)
            else:
                raise NameError("Wrong input")
        elif HideRandomiser == 0:
            CurrentRoom += 1
            print("Current room:", CurrentRoom)
    elif Chosen_Door != RightDoor:
        print("You died")
        break

if CurrentRoom == 10:
    if TakenKeyBack == "N":
        print("You didnt take the key with you and now cant return due to mobs,")
        print("After some time they catch you")
        print("")
        print("The END")
    elif TakenKeyBack == "J":
        print("You Exit to the final room")
        CurrentRoom = 11

while CurrentRoom == 11:
    print("You enter the room and see a lot of work tables and a baricaded door, You can see daylight trough the cracks")
    print("I need a tool to break down the baricade on the door")
    SearchTool = input("Choose to search the: shelve, workbench, floor")
    if SearchTool == "WorkBench":
        print("You found an axe")
        BreakTheDoor = input("Are you sure you want to break the door? This action can not be undone! J/N")
        if BreakTheDoor == "J":
            print("You win")
            CurrentRoom == 12
        else:
            print("You took to long and died")

    else:
        Randomiser = randint(1,2)
        if Randomiser == 1:
            print("You found a broken tool")
        
        elif Randomiser == 2:
            print("You found nothing")