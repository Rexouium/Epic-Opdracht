from calendar import weekday


DayOfTheWeek = input("Welke Dag is het? :").lower()

Weekdays = ["ma", "di", "wo", "do", "vr", "za", "zo"]
days = 0

while DayOfTheWeek != Weekdays[days]:
    print(Weekdays[days])
    days += 1
print(DayOfTheWeek)