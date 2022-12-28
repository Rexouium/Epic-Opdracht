from fruitmand import fruitmand
Fruitsoorten = []
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
for x in fruitmand:
    if x['color'] not in Fruitsoorten:
        Fruitsoorten.append(x['color'])
print(Fruitsoorten)
