from ProgramFunctions import *

order_safing = {}
aantalbollentjesvoor_rekenen = 0
aantalhoorentjesesvoor_rekenen = 0
aantalbakjesvoor_rekenen = 0

keep_ordering = True
# vars
IjsBollentje_Prijs_per_Bol = 1.10
Bakje_Prijs_per = 0.20
Hoorentje_Prijs_per = 0.20

Totale_bol_prijs = 0
Totale_hooren_prijs = 0
Totale_bak_prijs = 0
Full_TotalPrice = 0


while keep_ordering:
    bollen = hoe_veel_bollen_ijs("hoe veel bollen")
    Container_question = bakje_of_hoorentje(bollen)
    geef_bestelling_aan = bestellingteller(bollen, Container_question)
    AantallenDataStoreProcessor(Container_question, order_safing)

    aantalbollentjesvoor_rekenen = aantal_bollen_voor_bon(bollen, aantalbollentjesvoor_rekenen)
    print("Container question is:", Container_question)
    if Container_question == "hoorentje":
        aantalhoorentjesesvoor_rekenen = aantal_hoorentjes_voor_bon(aantalhoorentjesesvoor_rekenen)
    elif Container_question == "bakje":
        aantalbakjesvoor_rekenen = aantal_bakjes_voor_bon(aantalbakjesvoor_rekenen)

    Totale_bol_prijs = aantalbollentjesvoor_rekenen * IjsBollentje_Prijs_per_Bol
    Totale_bak_prijs = aantalbakjesvoor_rekenen * Bakje_Prijs_per
    Totale_hooren_prijs = aantalhoorentjesesvoor_rekenen * Hoorentje_Prijs_per

    Full_TotalPrice = round(Totale_bol_prijs + Totale_bak_prijs + Totale_hooren_prijs, 2)

    keep_ordering = orderfuncorstopfunc()

print(f"""
---------["Papi Gelato"]---------

Bollentjes: {aantalbollentjesvoor_rekenen} X {Totale_bol_prijs}
Hoorentjes: {aantalhoorentjesesvoor_rekenen} X {Totale_hooren_prijs}
Bakjes: {aantalbakjesvoor_rekenen} X {Totale_bak_prijs}

Total: {Full_TotalPrice}

""")
