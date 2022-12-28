from fruitmand import fruitmand

ListMomento = []
RondeFruit = {"round": 0, "notround": 0}

for x in fruitmand:
    if x['color'] not in ListMomento:
        ListMomento.append(x['color'])

while not (answer := input(f"Vertel ons een kleur uit de volgende opties: {', '.join(ListMomento)}")) in ListMomento:
    print("Die kleur bestaat niet in de fruitmand")

for x in fruitmand:
    if x['color'] == answer:

        if x['round']:
            RondeFruit['round'] += 1

        else:
            RondeFruit['notround'] += 1

if RondeFruit['round'] > RondeFruit['notround']:
    print(f"verschil is: {RondeFruit['round'] - RondeFruit['notround']} meer rondefuit dan niet rondefruit in kleur {answer}")
elif RondeFruit['round'] < RondeFruit['notround']:
    print(f"verschil is: {RondeFruit['notround'] - RondeFruit['round']} meer rondefuit dan niet rondefruit in kleur {answer}")
elif RondeFruit['round'] == RondeFruit['notround']:
    print(f"Niet rond en wel rond zijn hetzelfde in kleur {answer}")