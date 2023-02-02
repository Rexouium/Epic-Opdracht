def fibo_recursion(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursion(n-1) + fibo_recursion(n-2)


def fibo_loop(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            c = a + b
            a, b = b, c
        return b


def fibo_list(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        fibo = [0, 1]
        for i in range(2, n+1):
            fibo.append(fibo[i-1] + fibo[i-2])
        return fibo[n]

userinput = int(input("hoe veel keer de reeks?: "))
for i in range(userinput):
    print(fibo_list(i))
