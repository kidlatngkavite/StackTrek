grade = float(input("grade = "))

if (grade < 0) or (grade > 10) :
    print("Grades should be from zero to 10.")
else :
    halfPointCheck = grade%0.5
    if halfPointCheck != 0:
        print("Grades should be rounded to the nearest half point.")
    elif (grade <= 10) and (grade >= 8.5) :
        print("Grade A")
    elif (grade <= 8) and (grade >= 7.5) :
        print("Grade B")
    elif (grade <= 7) and (grade >= 6.5) :
        print("Grade C")
    elif (grade <= 6) and (grade >= 5.5) :
        print("Grade D")
    elif (grade <= 5.5) and (grade >= 0) :
        print("Grade F")