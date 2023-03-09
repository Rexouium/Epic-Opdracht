from ProgramFunctions import *
from DataStore import *

order_safing = {}
aantalbollentjesvoor_rekenen = 0
aantalhoorentjesesvoor_rekenen = 0
aantalbakjesvoor_rekenen = 0

keep_ordering = True
#vars
IjsBolPrijs[]



while keep_ordering:
    bollen = hoe_veel_bollen_ijs("hoe veel bollen")
    Container_question = bakje_of_hoorentje(bollen)
    geef_bestelling_aan = bestellingteller(bollen, Container_question)
    AantallenDataStoreProcessor(Container_question, order_safing)

    aantal_bollen_voor_bon(bollen, aantalbollentjesvoor_rekenen)

    keep_ordering = orderfuncorstopfunc()


