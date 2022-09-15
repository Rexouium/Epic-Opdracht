#Stel: je gaat met 3 vrienden (dus met zijn vieren) een dag naar de speelhal: ‘de Speelhal-dag’

#Dat kost een toegangsticket per persoon van 7,45 euro voor de hele dag. Jullie willen ook met zijn allen voor 45 minuten in de VIP-VR-GameSeat. De VIP-VR GameSeat kost per persoon 37 eurocent per 5 minuten. Jij trakteert dus betaal je alles.

#Maak een programma speelhal.py voor deze berekening.

#Lever hier het programma in en vergeet ook niet te committen en pushen!


AantalMensen = int(input("Hoeveel Mensen:"))
Total_VR_time = int(input("How manny minutes:"))

toegangsticketPrijs = 7.45
VR_Minute_prijs = 0.37

TotaalPrijs = ((AantalMensen * toegangsticketPrijs) + ((Total_VR_time / 5) * VR_Minute_prijs))

print("Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar:",TotaalPrijs, "Euro")
