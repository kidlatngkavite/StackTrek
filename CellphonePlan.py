FREECALL = 60
FREETEXT = 100
PRICE = 799
ADDITIONALMINUTE = 6.5
ADDITIONALTEXT = 1
ADDITIONALCHARGE = 25.00
TAX = 0.05


consumedCalls = int(input("Consumed Calls in minutes: "))
consumedTexts = int(input("Consumed Calls in minutes: "))


# Compute excess minutes
if consumedCalls > FREECALL :
    excessMinutesCharges = ADDITIONALMINUTE*(consumedCalls-FREECALL)
else :
    excessMinutesCharges = 0

# Compute excess texts
if consumedTexts > FREETEXT :
    excessSMSCharges = ADDITIONALTEXT*(consumedTexts-FREETEXT)
else :
    excessSMSCharges = 0

totalBillBeforeTax = PRICE + excessMinutesCharges + excessSMSCharges + ADDITIONALCHARGE
taxCharges = totalBillBeforeTax * TAX
totalBillAfterTax = totalBillBeforeTax + taxCharges

print(f"Call minutes: {consumedCalls:.1f}")
print(f"Text messages: {consumedTexts:.1f}")
print(f"Excess minute charges: {excessMinutesCharges:.2f}")
print(f"Excess SMS charges: {excessSMSCharges:.2f}")
print(f"911 fee: {ADDITIONALCHARGE:.2f}")
print(f"Tax: {taxCharges:.2f}")
print(f"Total bill: {totalBillAfterTax:.2f}")
