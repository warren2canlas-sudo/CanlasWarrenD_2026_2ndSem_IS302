name = input("Enter student name: ")

grade1 = float(input("Enter grade for Subject 1: "))
grade2 = float(input("Enter grade for Subject 2: "))
grade3 = float(input("Enter grade for Subject 3: "))

average = (grade1 + grade2 + grade3) / 3

# Determine remark
if average >= 90:
    remark = "Excellent"
elif average >= 85:
    remark = "Very Good"
elif average >= 80:
    remark = "Good"
elif average >= 75:
    remark = "Fair"
else:
    remark = "Failed"

print("\n----- STUDENT GRADE ANALYSIS -----")
print("Student Name:", name)
print("Average Grade:", round(average, 2))
print("Remark:", remark)