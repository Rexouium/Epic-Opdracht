Antwoord = 50
ErbijAntwoord = 51
PrintVariable = "50"

while Antwoord < 1000:
    Antwoord += ErbijAntwoord
    PrintVariable += "+" + str(ErbijAntwoord)
    print(PrintVariable, "=" , Antwoord)
    ErbijAntwoord += 1 # 4