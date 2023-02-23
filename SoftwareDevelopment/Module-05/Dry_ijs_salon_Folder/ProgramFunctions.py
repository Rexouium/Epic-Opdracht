def hoe_veel_bollen_ijs(text):
    while True:
        aantal = int(input(text))
        print(aantal)
        if aantal <= 8:
            print("Success")
            return aantal
        else:
            print("Minder dan 8, aub!")


def bakje_of_hoorentje(checker):
    waarinloop = True
    containertype = ""
    while waarinloop:
        if checker <= 4:
            while not (containertypevar := input("1 voor een bakje en 2 voor een hoorentje")).isdigit():
                print("Nummer alstublieft")
            if int(containertypevar) == 1:
                containertype = "bakje"
            else:
                containertype = "hoorentje"
            waarinloop = False
        elif checker > 4:
            containertype = "bakje"
            waarinloop = False
        else:
            print("Not an option here.")
    return containertype


def bestellingteller(hoeveelbollen, container):
    order = f"{container} met: {hoeveelbollen} bollen ijs"
    return order


def orderfuncorstopfunc():
    while True:
        while not (stopvar := input("1 voor meer bestellen en 2 om te stoppen met bestellen")).isdigit():
            print("Nummers, nerd.")
        if int(stopvar) == 1:
            print("Processing")
            return True
        else:
            return False
