telefoon1 = "iPhone_13"
telefoon2 = "samsung_Galaxy_S22"
telefoon3 = "Asus Zenphone 9"

iPhone_13 = int(input("Hoe duur is de iPhone 13? :"))
samsung_Galaxy_S22 = int(input("Hoe duur is de samsung_Galaxy_S22? :"))
Asus_Zenphone_9 = int(input("Hoe duur is de Asus_Zenphone_9? :"))

vershilprijs = (iPhone_13 - samsung_Galaxy_S22)
vershilprijs_alles = (iPhone_13 - samsung_Galaxy_S22 - Asus_Zenphone_9)
combinatie_prijs = (iPhone_13 + samsung_Galaxy_S22)

if iPhone_13 >= 900:
    print("de iPhone_13 Is het duurst, de telefoon kost:", iPhone_13, "Euro")
    print("de samsung_Galaxy_S22 Is het goedkoopst, de telefoon kost:", samsung_Galaxy_S22, "Euro")
    rekenVeriable = 0 #bugfix
elif samsung_Galaxy_S22 >= 900:
    print("de samsung_Galaxy_S22 Is het duurst, de telefoon kost:", samsung_Galaxy_S22, "Euro")
    print("de iPhone_13 Is het goedkoopst, de telefoon kost:", iPhone_13, "Euro")
    rekenVeriable = 0 #bugfix
elif iPhone_13 == samsung_Galaxy_S22:
    print("de samsung_Galaxy_S22 Is evenduur, de telefoon kost:", samsung_Galaxy_S22, "Euro")
    print("de iPhone_13 Is evenduur, de telefoon kost:", iPhone_13, "Euro")
    rekenVeriable = 0 #bugfix
########################################################################################################
elif iPhone_13 >= samsung_Galaxy_S22:
    print("de iPhone_13 Is het duurst, de telefoon kost:", iPhone_13, "Euro")
    print("de samsung_Galaxy_S22 Is het goedkoopst, de telefoon kost:", samsung_Galaxy_S22, "Euro")
    rekenVeriable = iPhone_13
    rekenVeriable -= 50
########################################################################################################
elif samsung_Galaxy_S22 >= iPhone_13:
    print("de samsung_Galaxy_S22 Is het duurst, de telefoon kost:", samsung_Galaxy_S22, "Euro")
    print("de iPhone_13 Is goedkoopst, de telefoon kost:", iPhone_13, "Euro")
    rekenVeriable = samsung_Galaxy_S22
    rekenVeriable -= 50
########################################################################################################
if  rekenVeriable <= samsung_Galaxy_S22:
    print("Het advies is dus de", telefoon1, "te kopen. Deze is namelijk:", vershilprijs, "Euro goedkoper dan de", telefoon2, "En binnen je budget")

if (rekenVeriable >= samsung_Galaxy_S22 and vershilprijs > 50 and (combinatie_prijs - Asus_Zenphone_9) >= 100):
    print("Het advies is dus de", telefoon3, "te kopen. Deze is namelijk:", vershilprijs_alles, "Euro duurder/goedkoper dan de", telefoon1, "En", telefoon2)
elif (rekenVeriable >= samsung_Galaxy_S22) and vershilprijs > 50 and not vershilprijs_alles >= 100:
    print("Het advies is dus de", telefoon2, "te kopen. Deze is namelijk:", vershilprijs, "Euro duurder/goedkoper dan de", telefoon1, "En buiten je budget van 50 euro verschil")

if samsung_Galaxy_S22 >= 900 and iPhone_13 >= 900 and Asus_Zenphone_9 >= 900:
    print("Het advies is dus geen telefoon te kopen ze zijn te duur")