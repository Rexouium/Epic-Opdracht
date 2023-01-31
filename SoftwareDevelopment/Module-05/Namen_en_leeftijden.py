infolist = {}
stopvar = " "


def listupdater():
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    infolist[name] = age


print()

while not stopvar == "y":
    listupdater()
    stopvar = input("Want to stop? Y or N").lower()

for x in infolist:
    print(f"{x} is {infolist[x]} jaar oud")
