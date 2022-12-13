import random
while not (aantal := input("Hoe veel m&m's?: ")).isdigit():
    print("Getal aub")
KleurLijst = ["rood", "blauw", "groen", "geel", "bruin"]
MenM = {}
for x in range(int(aantal)):
    Keuze = random.choice(KleurLijst)
    print(Keuze)
    if Keuze in MenM:
        MenM[Keuze] += 1
        print("Updating Kleur")
    else:
        print("Kleur Toevoegen")
        MenM[Keuze] = 1
print(MenM)