def reeksstuff():
    howmuch = int(input("How many terms? "))
    number1, number2 = 0, 1
    count = 0
    if howmuch <= 0:
        print("Please enter a positive integer")
    elif howmuch == 1:
        print("Fibonacci sequence upto", howmuch, ":")
        print(number1)
    else:
        print("Fibonacci sequence:")
        while count < howmuch:
            print(number1)
            nth = number1 + number2
            number1 = number2
            number2 = nth
            count += 1


reeksstuff()
