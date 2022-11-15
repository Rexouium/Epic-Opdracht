import random

ListVariable = ["Text0", "Text1", "Text2", "Text3", "Text4"]
RandomNumber = random.randint(0,4)

if RandomNumber == 1:
    print(random.choice(ListVariable))
    print(ListVariable)