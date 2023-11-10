amount = int(input("amount in cents: "))
dollars = amount//100
quarters = (amount % 100)//25
dimes = ((amount % 100) % 25) // 10
nickels = (((amount % 100) % 25) % 10) // 5
pennies = ((((amount % 100) % 25) % 10) % 5) // 1

print(f"{(amount/100)} consists of:")
print(f"Dollars: {dollars}")
print(f"Quarters: {quarters}")
print(f"Dimes: {dimes}")
print(f"Nickels: {nickels}")
print(f"Pennies: {pennies}")