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
#Tegels berekenen
###########################################################################
TegelKleur = input("Normaal, Rood, NaarKeuze").lower()

TegelPrijsPerm2 = 250
if TegelKleur == "normaal":
    if GroteZwembad < 20:
        TegelPrijsPerm2 = 250
    elif GroteZwembad >= 20:
        TegelPrijsPerm2 = 200

elif TegelKleur == "rood":
    if GroteZwembad < 20:
        TegelPrijsPerm2 = 275
    elif GroteZwembad >= 20:
        TegelPrijsPerm2 = 220

elif TegelKleur == "naarkeuze":
    if GroteZwembad < 20:
        TegelPrijsPerm2 = 350
    elif GroteZwembad >= 20:
        TegelPrijsPerm2 = 325



HoeveelGrond = Lengte * Breedte * Hoogte

AfgevoerdeGrondTotaalPrijs = HoeveelGrond * AfgevoerdeGrondPrijs
UitGraafKostenPrijs = UitGraafKosten * GroteZwembad
TegelTotaalPrijs = TegelPrijsPerm2 * (Lengte * Breedte)
TotaalPrijs = (EindPrijsKilometers + UitGraafKostenPrijs + TegelTotaalPrijs + AfgevoerdeGrondTotaalPrijs)
print(" ")
print(" ")
print("Uitgraaf kosten =", UitGraafKostenPrijs, "Euro")
print("Afvoeren Grond =", AfgevoerdeGrondTotaalPrijs, "Euro")
print("Voor rij kosten =", EindPrijsKilometers, "Euro")
print("Beton + Tegel kosten =", TegelTotaalPrijs)
print("Totaal =", TotaalPrijs, "Euro")