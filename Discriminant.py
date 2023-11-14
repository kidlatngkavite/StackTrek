from math import sqrt

aCoeff = float(input("a = "))
bCoeff = float(input("b = "))
cCoeff = float(input("c = "))

discriminant = bCoeff**2 - 4*aCoeff*cCoeff

if aCoeff == 0 and bCoeff != 0:
    ans = -cCoeff/bCoeff
    print(f"Solution: {ans:.3f}")
elif (aCoeff == 0 and bCoeff == 0) :
    print("No unknown")
elif discriminant < 0 :
    print("No solutions")
elif discriminant == 0 :
    ans = -bCoeff/(2*aCoeff)
    print(f"Solution: {ans:.3f}") 
elif discriminant > 0 :
    ans1 = (-bCoeff + sqrt(discriminant) )/(2*aCoeff)
    ans2 = (-bCoeff - sqrt(discriminant) )/(2*aCoeff)
    print(f"Solutions: {ans1:.3f} and {ans2:.3f}") 