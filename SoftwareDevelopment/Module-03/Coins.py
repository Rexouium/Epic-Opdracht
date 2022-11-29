# name of student: mitchel
# number of student: 99071642
# purpose of program: 
# function of program:
# structure of program: 
TotalCoins_500 = 0
TotalCoins_200 = 0
TotalCoins_100 = 0
TotalCoins_50 = 0
TotalCoins_20 = 0
TotalCoins_10 = 0
TotalCoins_5 = 0
TotalCoins_2 = 0
TotalCoins_1 = 0
CoinNumberCheck = 0

NotEnoughChange = 0

toPay = int(float(input('Amount to pay: '))* 100) # input waar je een getal invult voor wat je moet betalen
paid = int(float(input('Paid amount: ')) * 100) # input voor wat je betaald
change = paid - toPay # berekent wat je terug krijgt

if change > 0: # kijkt of de "change" meer is dan 0
  coinValue = 500 # zet de waarde naar 50
  
  while change > 0 and coinValue > 0: # loops tot dat bijde 0 zijn
    nrCoins = change // coinValue # deelt change door coinvalue
    CoinNumberCheck = 0
    if NotEnoughChange > 0:
      print("Not enough change!")
    else:
      print("")

    if nrCoins > 0: # checkt of nrcoins meer is dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) #print wat je terug moet geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # print wat je geeft
      change -= nrCoinsReturned * coinValue # haalt de totaal waarden van (nrcoins keer coin value) af van change
      CoinNumberCheck += nrCoinsReturned
      if change > 0:
        NotEnoughChange += 1
      else:
        NotEnoughChange = 0

      if coinValue == 500:
        TotalCoins_500 = CoinNumberCheck
      elif coinValue == 200:
        TotalCoins_200 = CoinNumberCheck
      elif coinValue == 100:
        TotalCoins_100 = CoinNumberCheck
      elif coinValue == 50:
        TotalCoins_50 = CoinNumberCheck
      elif coinValue == 20:
        TotalCoins_20 = CoinNumberCheck
      elif coinValue == 10:
        TotalCoins_10 = CoinNumberCheck
      elif coinValue == 5:
        TotalCoins_5 = CoinNumberCheck
      elif coinValue == 2:
        TotalCoins_2 = CoinNumberCheck
      elif coinValue == 1:
        TotalCoins_1 = CoinNumberCheck
###########################
# comment on code below: verandert de coin waardens
    if coinValue == 500:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 100
    elif coinValue == 100:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0

if change > 0: # checkt of change meer is dan 0
  print('Change not returned: ', str(change) + ' cents')
else:
  print(TotalCoins_500, "5 Euro munten")
  print(TotalCoins_200, "2 Euro munten")
  print(TotalCoins_100, "1 Euro munten")
  print(TotalCoins_50, "50 Cent munten")
  print(TotalCoins_20, "20 Cent munten")
  print(TotalCoins_10, "10 Cent munten")
  print(TotalCoins_5, "5 Cent munten")
  print(TotalCoins_2, "2 Cent munten")
  print(TotalCoins_1, "1 Cent munten")
  print('done')