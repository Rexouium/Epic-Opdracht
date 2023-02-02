import random

game = True
points = 0

while game:
    def getZone(item: str) -> str:
        inputSentence = ""
        genNumber = random.randint(1, (3 if item != "vent" else 2))
        print(genNumber)

        if item == "crowbar" or item == "key":
            inputSentence = f"1 for under the {'bed' if item == 'key' else 'worktable'}, 2 for in the {'closet' if item == 'key' else 'cabinet'} and 3 for on the {'floor' if item == 'keyy' else 'table'}"
        elif item == "door":
            inputSentence = "Door 1, 2 or 3?"
        elif item == "vent":
            inputSentence = "1 to open the vent, 2 to wait 5 minutes and then open the vent:"

        while not (choice := input(inputSentence)).isdigit():
            print("Please provide one of the mentioned numbers.")

        choice = int(choice)

        if choice == genNumber:
            print(
                f"Congratulations! {f'You found {item}' if item == 'crowbar' or item == 'key' else f'You opened the {item} to the next area'}")
            return "point"
        else:
            print(f"Oh no... You're a fucking idiot and you died...")

    while points < 20:
        print("points: ", points)
        genNumber = random.randint(1, 18)
        if genNumber > 0 and genNumber < 7:
            if getZone("key") == "point":
                points += 1
            else:
                points = 20
        elif genNumber > 6 and genNumber < 13:
            if getZone("door") == "point":
                points += 1
            else:
                points = 20
        else:
            if getZone("crowbar") == "point":
                points += 1
            else:
                points = 20
            if points < 20:
                if getZone("vent") == "point":
                    points += 1
                else:
                    points = 20

    replay = ""
    while not (replay == "y" or replay == "n"):
        replay = input("Would you like to play again?")

    if replay == "y":
        points = 0
        choice = ""
    else:
        print(f"Good job. You ended with {points} points")
        game = False
