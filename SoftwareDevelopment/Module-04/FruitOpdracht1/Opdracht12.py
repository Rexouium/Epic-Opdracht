from fruitmand import fruitmand

translator = []


def translation(fruitcolor: str) -> str:
    translator = {"yellow": "geel", "green" : "groen", "orange" : "oranje", "brown" : "bruin"}
    if fruitcolor in translator:
        return translator[fruitcolor]
    else:
        return fruitcolor


lengte = []

for x in fruitmand:
    lengte.append(len(x['name']))

index = lengte.index(max(lengte))
langstefruit = fruitmand[index]

print(f"{langstefruit['name']} ({len(langstefruit['name'])} letters) heeft een {translation(langstefruit['color'])} kleur en een gewicht van: {langstefruit['weight'] / 1000} kg")
