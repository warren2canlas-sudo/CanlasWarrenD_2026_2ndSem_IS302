grades_list = []

# Input 5 grades
for count in range(5):
    grade_input = float(input(f"Enter grade {count + 1}: "))
    grades_list.append(grade_input)

# Compute values
average_grade = sum(grades_list) / len(grades_list)
highest_grade = max(grades_list)
lowest_grade = min(grades_list)

# Display results
print("\nGrade Analysis Results:")
print("Average Grade:", average_grade)
print("Highest Grade:", highest_grade)
print("Lowest Grade:", lowest_grade)