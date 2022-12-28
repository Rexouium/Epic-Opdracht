from fruitmand import fruitmand
for idx, dictionary in enumerate(fruitmand):
    if dictionary['name'] == "appel":
        print("De appel weegt: " + str(dictionary['weight']) + 'g')