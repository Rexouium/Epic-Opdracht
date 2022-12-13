#Antwoord = 50
#ErbijAntwoord = 51
#PrintVariable = "50"

Antwoord2 = int(input("Eerste getal"))
ErbijAntwoord2 = Antwoord2 + 1
PrintVariable2 = str(Antwoord2)



while Antwoord2 < 1000:
    Antwoord2 += ErbijAntwoord2
    PrintVariable2 += "+" + str(ErbijAntwoord2)
    print(PrintVariable2, "=" , Antwoord2)
    ErbijAntwoord2 += 1 # 4