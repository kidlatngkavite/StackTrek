costEgg = 7
costTray = 70
numberEggs = int(input("How many Eggs: "))
print(f"{((numberEggs//12)*costTray) + ((numberEggs%12)*costEgg)}")

