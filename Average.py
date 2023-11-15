#initialization
countofNumbers = 0
entry = 0
sum = 0

# Get sum of all entries and iterate countofNumers every loop
while True :
    entry = int(input(f"Entry {countofNumbers+1}: "))
    if entry == 0:
        break
    sum += entry
    countofNumbers += 1

#convert to intger then print
average = int(sum/countofNumbers)
print(f"{average}")
