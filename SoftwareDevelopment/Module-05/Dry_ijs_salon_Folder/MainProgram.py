from ProgramFunctions import *
gekozensmaken = ["vanile"]
order_safing = []
keep_ordering = True

while keep_ordering:
    bollen = hoe_veel_bollen_ijs("hoe veel bollen")
    Container_question = bakje_of_hoorentje(bollen)
    geef_bestelling_aan = bestellingteller(bollen, Container_question)
    order_safing.append(bestellingteller(bollen, Container_question))
    print(order_safing)
    keep_ordering = orderfuncorstopfunc()
