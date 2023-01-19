import random
NameHolder = []
RandomNameList = []
CounterForNames = 0
NameAmountInput = int(input("Say hoe veel namen je wilt invullen"))
while CounterForNames < NameAmountInput:
    NameInporter = input("Say name")
    if NameInporter in NameHolder:
        print("Try again")
    elif NameInporter != NameHolder:
        CounterForNames += 1
        RandomNameList.append(NameInporter)
        NameHolder.append(NameInporter)
x = 0
listamount = len(NameHolder)
while x != len(NameHolder):
    x = 0
    for x in range(listamount):
        if NameHolder[x] == RandomNameList[x]:
            random.shuffle(RandomNameList)
            print("shuffled")
        else:
            x += 1
for x in range(listamount):
    print(f"{NameHolder[x]} heeft {RandomNameList[x]}")
