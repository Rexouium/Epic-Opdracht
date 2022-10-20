from os import name
import random
Name = input("Vull je naam in")
Number = random.randint(1, 3)

if Number == 1:
    print("You are smart", Name)
elif Number == 2:
    print("er is niks te verbeteren", Name)
else:
    print("Je bent goed bezig:", Name)