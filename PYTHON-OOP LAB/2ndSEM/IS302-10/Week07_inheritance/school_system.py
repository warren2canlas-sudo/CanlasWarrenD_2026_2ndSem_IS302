class Person_wdc:
    def __init__(self_wdc, name_wdc, age_wdc):
        self_wdc.name_wdc = name_wdc
        self_wdc.age_wdc = age_wdc

    def display_info_wdc(self_wdc):
        print("Name:", self_wdc.name_wdc)
        print("Age:", self_wdc.age_wdc)


class Student_wdc(Person_wdc):
    def __init__(self_wdc, name_wdc, age_wdc, course_wdc):
        super().__init__(name_wdc, age_wdc)
        self_wdc.course_wdc = course_wdc

    def display_info_wdc(self_wdc):
        super().display_info_wdc()
        print("Course:", self_wdc.course_wdc)


class Teacher_wdc(Person_wdc):
    def __init__(self_wdc, name_wdc, age_wdc, subject_wdc):
        super().__init__(name_wdc, age_wdc)
        self_wdc.subject_wdc = subject_wdc

    def display_info_wdc(self_wdc):
        super().display_info_wdc()
        print("Subject:", self_wdc.subject_wdc)


# Example usage
student_wdc = Student_wdc("Warren", 20, "BSIS")
teacher_wdc = Teacher_wdc("Mr. Can;as", 45, "Mathematics")

print("Student Info:")
student_wdc.display_info_wdc()
print("\nTeacher Info:")
teacher_wdc.display_info_wdc()

#Warren GRADES100