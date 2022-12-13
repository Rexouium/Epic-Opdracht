#Groep A

GRP_A_Land1 = input("Land 1 =")
GRP_A_Land2 = input("Land 2 =")
GRP_A_Land3 = input("Land 3 =")


GoalsMatch1GRP1 = int(input(f"Score for{GRP_A_Land1}"))
GoalsMatch1GRP2 = int(input(f"Score for{GRP_A_Land2}"))

GoalsMatch2GRP2 = int(input(f"Score for{GRP_A_Land2}"))
GoalsMatch2GRP3 = int(input(f"Score for{GRP_A_Land3}"))

GoalsMatch3GRP1 = int(input(f"Score for{GRP_A_Land1}"))
GoalsMatch3GRP3 = int(input(f"Score for{GRP_A_Land3}"))


#uitkomst matches

print(GRP_A_Land1, "Thuis vs", GRP_A_Land2, "Uit,  Score =", GoalsMatch1GRP1,"-",GoalsMatch1GRP2)
print(GRP_A_Land2, "Thuis vs", GRP_A_Land3, "Uit,  Score =", GoalsMatch2GRP2,"-",GoalsMatch2GRP3)
print(GRP_A_Land1, "Thuis vs", GRP_A_Land3, "Uit,  Score =", GoalsMatch3GRP1,"-",GoalsMatch3GRP3)

if GoalsMatch1GRP1 > GoalsMatch3GRP1:
    DoelSaldoGRP1 = GoalsMatch1GRP2 - GoalsMatch3GRP1
else:
    DoelSaldoGRP1 = GoalsMatch3GRP1 - GoalsMatch1GRP1



if GoalsMatch1GRP2 > GoalsMatch2GRP2:
    DoelSaldoGRP2 = GoalsMatch1GRP2 - GoalsMatch2GRP2
    print(DoelSaldoGRP2,"test")
else:
    DoelSaldoGRP2 = GoalsMatch2GRP2 - GoalsMatch1GRP2
    print(DoelSaldoGRP2)


if GoalsMatch2GRP3 > GoalsMatch3GRP3:
    DoelSaldoGRP3 = GoalsMatch2GRP3 - GoalsMatch3GRP3
else:
    DoelSaldoGRP3 = GoalsMatch3GRP3 - GoalsMatch2GRP3
