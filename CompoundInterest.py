principal = float(input("Loan Amount: "))
interestRate = float(input("Interest Rate: "))
years = int(input("Years: "))

print(f"{(principal)*((1+(interestRate/100))**years):.2f}")