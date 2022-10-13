RijAfstand = int(input("Hoe veel Kilometers:"))
GroteZwembad = int(input("Hoe veel vierkantemeters:"))
Lengte = float(input("Hoelang:"))
Hoogte = float(input("HoeHoog"))
Breedte = float(input("HoeBreed"))

VastePrijs = 0
PrijsPerKilometers = 0
UitGraafKosten = 25
AfgevoerdeGrondPrijs =32.50

###########################################################################
if RijAfstand < 50 and GroteZwembad < 20:
    VastePrijs = 100
    PrijsPerKilometers = 1.25
    PrijsPerKilometers += (RijAfstand * PrijsPerKilometers)
elif RijAfstand >= 50 and GroteZwembad < 20:
    VastePrijs = 100
    PrijsPerKilometers = 1.15
    PrijsPerKilometers += (RijAfstand * PrijsPerKilometers)
elif RijAfstand < 50 and GroteZwembad >= 20:
    VastePrijs = 250
    PrijsPerKilometers = 2.15
    PrijsPerKilometers += (RijAfstand * PrijsPerKilometers)
elif RijAfstand >= 50 and GroteZwembad >= 20:
    VastePrijs = 250
    PrijsPerKilometers = 2.05
    PrijsPerKilometers += (RijAfstand * PrijsPerKilometers)
###########################################################################

HoeveelGrond = Lengte * Breedte * Hoogte
print("Hoeveel grond =", HoeveelGrond, "M3" )#AfgevoerdeGrondPrijs, "Euro")