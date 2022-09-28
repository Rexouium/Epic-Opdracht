a = int(input("Nummer1"))
b = int(input("Nummer2"))

rekengetal1 = 0
rekengetal2 = 0

if a == b:
    print("Bijde getallen zijn gelijk")
elif a >= b:
    rekengetal1 += a
    rekengetal2 += b
elif b >= a:
    rekengetal1 += b
    rekengetal2 += a

print("Het minimum is:", rekengetal2, "En de max is:", rekengetal1)