Container = ("Maandag", "Dinsdag", "Woensdag", "Donderdag", "Vrijdag", "Zaterdag", "Zondag")
#alle dagen
print("alles")
print(Container)
print("Werkdagen")
#werk dagen
for x in range(5):
    print(Container[x])
#WeekendDagen
WeekendDagen = 5
print("Weekend")
for i in range(2):
    print(Container[WeekendDagen])
    WeekendDagen += 1
print("Dagen omgekeerd")
OmkerenContainer = Container
result = reversed(OmkerenContainer)
result = tuple(result)
print(result)
print("Werkdagen omgekeerd")
teller = 4
for h in range(5):
    print(Container[teller])
    teller -= 1
print("Weekend omgekeerd")
tellerWeekend = 6
for g in range(2):
    print(Container[tellerWeekend])
    tellerWeekend -= 1
