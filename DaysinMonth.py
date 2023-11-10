month = int(input("Month Number: "))



if (month%12) == 2:
    print("28 or 29 days")
elif (month%12) == 4 or (month%12) == 6 or (month%12) == 9 or (month%12) == 11:
    print("30 days")
else:
    print("31 days")