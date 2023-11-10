athlete1 = int(input("Time of Athlete 1 in seconds"))
athlete2 = int(input("Time of Athlete 2 in seconds"))
athlete3 = int(input("Time of Athlete 3 in seconds"))

total = athlete1+athlete2+athlete3
minutes = total//60
seconds = (total%60)
print(f"{minutes}:{seconds:02d}")