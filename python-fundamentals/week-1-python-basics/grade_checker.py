gradePercent = int(input("Enter grade percent: "))

if gradePercent >= 90:
    grade = "A"
elif gradePercent >= 80:
    grade = "B"
elif gradePercent >= 70:
    grade = "C"
elif gradePercent >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)