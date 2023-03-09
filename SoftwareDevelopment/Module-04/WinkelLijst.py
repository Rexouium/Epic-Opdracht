ShopList = {}
WhileValue = True

while WhileValue:
    UserInput = input("Item Name: ")
    UserAmountInput = int(input("Hoeveel: "))

    if UserInput in ShopList:
        ShopList.update({UserInput: UserAmountInput+ShopList[UserInput]})
    else:
        ShopList[UserInput] = UserAmountInput

    StopInput = input("Veder? ja of nee").lower()
    if StopInput == "ja":
        print("Loading")
    else:
        WhileValue = False

for x in ShopList.keys():
    print(f"{str(ShopList[x])}x {x.capitalize()}")
