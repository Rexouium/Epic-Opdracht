#mitchel brederije
#Pizza calculator
from distutils.log import error
import random
OrderNumber = random.randint(100, 999)


Small_Aantal = 0
Medium_Aantal = 0
Large_Aantal = 0

while True:

    Small_Price = 8.00
    Medium_Price = 10.00
    Large_Price = 15.00

  

    try:
        print("Small", Small_Price,"Medium", Medium_Price,"Large", Large_Price)
        Pizza_Grote = input("Hoe groot? (Options above only) :").lower()
    except:
        print(error) 
###############################################
    try:
        if (Pizza_Grote == "small"):
            Hoeveel_Small_pizza = int(input("Hoeveel_Small_pizza :"))

            Small_Aantal += Hoeveel_Small_pizza

        Continueorstop = str(input("More or Stop"))
    except:
        print(error)
###############################################
    try:
        if (Pizza_Grote == "medium"):
           Hoeveel_Medium_pizza = int(input("Hoeveel_Medium_pizza :"))
           Medium_Aantal += Hoeveel_Medium_pizza

           Continueorstop = str(input("More or Stop"))
    except:
        print(error)
###############################################
    try:
        if (Pizza_Grote == "large"):
            Hoeveel_Large_pizza = int(input("Hoeveel_Large_pizza :"))

            Large_Aantal += Hoeveel_Large_pizza
        
            Continueorstop = (input("More or Stop"))

        if (Continueorstop == "Stop" or Continueorstop == "stop"):
            break
        if (Continueorstop == "More" or Continueorstop == "more"):
            print("Processing")
        if (Continueorstop != "more" and Continueorstop != "More" and Continueorstop != "Stop" and Continueorstop != "stop"):
            print(error)
            break
    except:
        print(error)
###############################################

SmallTotaalPrijs = (Small_Price * Small_Aantal)
mediumTotaalPrijs = (Medium_Price * Medium_Aantal)
LargeTotaalPrijs = (Large_Price * Large_Aantal)

TotaalPrijs = (SmallTotaalPrijs + mediumTotaalPrijs + LargeTotaalPrijs)

print(" ")
print ("Order Number:", OrderNumber,"-----------")
print ("-----------------------------")
print ("Small Pizza's", Small_Aantal,"Stuks,", Small_Price, "Euro Stuk prijs")
print ("Medium Pizza's", Medium_Aantal,"Stuks,", Medium_Price, "Euro Stuk prijs")
print ("Large Pizza's", Large_Aantal,"Stuks,", Large_Price, "Euro Stuk prijs")
print ("-----------------------------")
print (TotaalPrijs, "Euro")
print ("-----------------------------")






#def get_answer(vraag: str) -> int:

#antwoord = 0

#while True:

#try:

#Antwoord = int(input(vraag))

#break

#exept valueError

#print("Probeer opnieuw")

#return antwoord



#print("Hoe ood ben je?")