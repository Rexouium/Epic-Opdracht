def addition(num1: int, num2: int, userchoice) -> float:
    if userchoice == 1:
        total = num1 + num2
    else:
        total = num1 + 2
    print(total)
    return total


def subtraction(num1: int, num2: int, userchoice) -> float:
    if userchoice == 1:
        total = num1 - num2
    else:
        total = num1 - 2
    print(total)
    return total


def multiplication(num1: int, num2: int, userchoice) -> float:
    if userchoice == 1:
        total = num1 * num2
    else:
        total = num1 * 2
    print(total)
    return total


def division(num1: int, num2: int, userchoice) -> float:
    if userchoice == 1:
        total = num1 / num2
    else:
        total = num1 / 2
    print(total)
    return total


choise = True

while choise:
    Question = int(input("""
    1: optellen = 1, 1
    2: aftrekken = 2, 1
    3: vermenigvuldigen = 3, 1
    4: delen = 4, 1
    5: ophogen = 1, 2
    6: verlagen = 2, 2
    7: verdubbelen = 3, 2
    8: halveren = 4, 2
    """))
    userchoice = int(input("1 voor advanced options 2 for basic"))
    number1 = None
    if number1 == None:
        number1 = float(input("num 1?"))
    number2 = float(input("num 2?"))
    yourmom = int()
    if Question > 4:
        print("please only input the right numbers for the options")
    elif Question == 1:
        yourmom = addition(number1, number2, userchoice)
    elif Question == 2:
        yourmom = subtraction(number1, number2, userchoice)
    elif Question == 3:
        multiplication(number1, number2, userchoice)
    elif Question == 4:
        division(number1, number2, userchoice)
    stopvar = input("y to stop or n to continue").lower()

    if stopvar == "y":
        choise = False
    elif stopvar == "n":
        Chooser = int(input("1 for new number and 2 for past total number"))
        if Chooser == 2:
            number1 = yourmom
        else:
            number1 = None
