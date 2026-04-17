class Student:
    def __init__(self, student_name, student_id, student_course):
        self.student_name = student_name
        self.student_id = student_id
        self.student_course = student_course

    def display_student(self):
        print("Name:", self.student_name)
        print("Student ID:", self.student_id)
        print("Course:", self.student_course)


# Create an object
student1 = Student("Juan Dela Cruz", "2025-001", "BSIS")

# Display student information
student1.display_student()