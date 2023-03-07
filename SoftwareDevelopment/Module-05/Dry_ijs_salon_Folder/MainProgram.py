from ProgramFunctions import *

order_safing = []
aantalbollentjesvoor_rekenen = 0
aantalhoorentjesesvoor_rekenen = 0
aantalbakjesvoor_rekenen = 0

keep_ordering = True

while keep_ordering:
    bollen = hoe_veel_bollen_ijs("hoe veel bollen")
    Container_question = bakje_of_hoorentje(bollen)
    geef_bestelling_aan = bestellingteller(bollen, Container_question)
    order_safing.append(bestellingteller(bollen, Container_question))

    aantal_bollen_voor_bon(bollen, aantalbollentjesvoor_rekenen)

    keep_ordering = orderfuncorstopfunc()

print('\n'.join(order_safing))
print(aantalbollentjesvoor_rekenen)
