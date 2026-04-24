class Student:
    def __init__(self, apd_name, apd_student_id, apd_gpa):
        # Private attributes with apd_ prefix
        self.__apd_name = apd_name
        self.__apd_student_id = apd_student_id
        self.__apd_gpa = apd_gpa

    def get_student_info(self):
        # Method to display all private information
        print(f"Name: {self.__apd_name}")
        print(f"Student ID: {self.__apd_student_id}")
        print(f"GPA: {self.__apd_gpa}")

# Creating an instance of Student
apd_student1 = Student("Juan", "2023-001", 1.75)

# Calling the method to display the info
apd_student1.get_student_info()


#warren