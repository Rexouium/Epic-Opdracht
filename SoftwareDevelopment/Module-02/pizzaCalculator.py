#mitchel brederije
#Pizza calculator
import random
OrderNumber = int(random.randint(100, 999))


Small_Aantal = 0
Medium_Aantal = 0
Large_Aantal = 0

while True:

    Small_Price = 8.00
    Medium_Price = 10.00
    Large_Price = 15.00

  


    print("Small 8.00, Medium 10.00, Large 15.00")
    Pizza_Grote = input("Hoe groot? (Options above only) :").lower()
###############################################
    if (Pizza_Grote == "small"):
        Hoeveel_Small_pizza = int(input("Hoeveel_Small_pizza :"))

        Small_Aantal += Hoeveel_Small_pizza

        Continueorstop = str(input("More or Stop"))
    
###############################################
    if (Pizza_Grote == "medium"):
        Hoeveel_Medium_pizza = int(input("Hoeveel_Medium_pizza :"))

        Medium_Aantal += Hoeveel_Medium_pizza

        Continueorstop = str(input("More or Stop"))
###############################################
    if (Pizza_Grote == "large"):
        Hoeveel_Large_pizza = int(input("Hoeveel_Large_pizza :"))

        Large_Aantal += Hoeveel_Large_pizza
    
        Continueorstop = (input("More or Stop"))

    if (Continueorstop == "Stop" or Continueorstop == "stop"):
        break
    if (Continueorstop != "Stop" or Continueorstop != "stop"):
        print("Processing")
###############################################

SmallTotaalPrijs = (Small_Price * Small_Aantal)
mediumTotaalPrijs = (Medium_Price * Medium_Aantal)
LargeTotaalPrijs = (Large_Price * Large_Aantal)

TotaalPrijs = (SmallTotaalPrijs + mediumTotaalPrijs + LargeTotaalPrijs)


print ("Order Number:", OrderNumber,"-------")
print ("-----------------------------")
print ("Small Pizza's", Small_Aantal)
print ("Medium Pizza's", Medium_Aantal)
print ("Large Pizza's", Large_Aantal)
print ("-----------------------------")
print (TotaalPrijs, "Euro")
print ("-----------------------------")