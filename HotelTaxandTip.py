TAX = 0.12
EMERGENCYFUND = 0.10
ACCOMODATION = 0.9

amount = float(input("Amount: "))
Remaining = amount*(1-TAX)
print(f"Tax: {(amount*TAX):.2f}")
print(f"Emergency Fund: {(Remaining*EMERGENCYFUND):.2f}")
print(f"Accommodation: {(Remaining*ACCOMODATION):.2f}")