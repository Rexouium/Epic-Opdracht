from fruitmand import fruitmand

def weight(e):
    return e['weight']

fruitmand.sort(key=weight, reverse=True)
for x in fruitmand:
    print(f"Het gewicht van een {x['name']} is {x['weight']/1000:.2f} Kilogram")