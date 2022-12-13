import random
#M&M's Systems
LegeList = []
KleurLijst = ("oranje", "blauw", "groen", "bruin")
MenMAantal = int(input("Hoe veel m en m's:  "))

kleurAantal = len(KleurLijst)

print(kleurAantal)

WhileValue = True

while WhileValue:
    ChoosingMENM = random.choice(KleurLijst)
    LegeList.append(ChoosingMENM)
    if len(LegeList) == MenMAantal:
        WhileValue = False


print(f"In de zak zitten de volgende emenems: {', '.join(LegeList)}")