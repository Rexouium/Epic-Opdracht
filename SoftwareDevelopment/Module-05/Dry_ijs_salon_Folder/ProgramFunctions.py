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
    while True:
        if checker <= 4:
            containertypevar = int(input("1 voor een bakje en 2 voor een hoorentje"))
            if containertypevar == 1:
                containertype = "bakje"
            else:
                containertype = "hoorentje"
            break
        elif checker > 4:
            containertype = "bakje"
            break
        else:
            print("Not an option here.")
    return containertype


def bestellingteller(hoeveelbollen, container):
    order = [f"{container} met: {hoeveelbollen} bollen ijs"]
    return order


def orderfuncorstopfunc():
    while True:
        stopvar = int(input("1 voor meer bestellen en 2 om te stoppen met bestellen"))
        if stopvar == 1:
            print("Processing")
            return True
        else:
            return False
