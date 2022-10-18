Time = 0

for i in range(0,25):
    if i < 13:
        print(i,":00 AM")
        Time += 1
    elif i < 25 and i > 12:
        print(i, ":00 PM")
        i += 1