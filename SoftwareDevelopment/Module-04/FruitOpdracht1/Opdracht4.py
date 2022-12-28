import random
from fruitmand import fruitmand
UserInput = int(input("Aantal fruit?: "))
FruitName = fruitmand
for x in range(UserInput):
    print(random.choice(fruitmand)['name'])
