from fruitmand import fruitmand
Total = 0
for x in fruitmand:
    RekenVar = 0
    if x['weight']:
        RekenVar = x['weight']
        Total += RekenVar
print("The total is: ", Total)