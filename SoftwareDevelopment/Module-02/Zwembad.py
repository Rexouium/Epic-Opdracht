RijAfstand = int(input("Hoe veel Kilometers:"))
Lengte = float(input("Hoelang:"))
Hoogte = float(input("HoeHoog"))
Breedte = float(input("HoeBreed"))

GroteZwembad = (Lengte * Breedte * Hoogte)
VastePrijs = 0
EindPrijsKilometers = 0
UitGraafKosten = 25
AfgevoerdeGrondPrijs =32.50

###########################################################################
if RijAfstand < 50 and GroteZwembad < 20:
    VastePrijs = 100
    PrijsPerKilometers = 1.25
    EindPrijsKilometers = (RijAfstand * PrijsPerKilometers)
elif RijAfstand >= 50 and GroteZwembad < 20:
    VastePrijs = 100
    PrijsPerKilometers = 1.15
    EindPrijsKilometers = (RijAfstand * PrijsPerKilometers)
elif RijAfstand < 50 and GroteZwembad >= 20:
    VastePrijs = 250
    PrijsPerKilometers = 2.15
    EindPrijsKilometers = (RijAfstand * PrijsPerKilometers)
elif RijAfstand >= 50 and GroteZwembad >= 20:
    VastePrijs = 250
    PrijsPerKilometers = 2.05
    EindPrijsKilometers = (RijAfstand * PrijsPerKilometers)
###########################################################################

HoeveelGrond = Lengte * Breedte * Hoogte
print("Uitgraaf kosten =", UitGraafKosten * GroteZwembad, "Euro")
print("Afvoeren Grond =", HoeveelGrond * AfgevoerdeGrondPrijs, "Euro")
print("Voor rij kosten =", EindPrijsKilometers, "Euro")
print("Totaal =", EindPrijsKilometers + HoeveelGrond, "Euro")