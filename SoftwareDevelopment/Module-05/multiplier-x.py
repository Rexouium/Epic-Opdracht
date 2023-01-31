m = int(input("Wat multiply je?"))
countervar = 0


def multiplier(m, countervar):
    for x in range(11):
        print(f"{m} X {countervar} = ", m * countervar)
        countervar += 1


multiplier(m, countervar)