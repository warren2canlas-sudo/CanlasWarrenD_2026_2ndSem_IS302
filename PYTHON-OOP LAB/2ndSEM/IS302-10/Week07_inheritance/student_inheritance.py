class Person_wdc:
    def __init__(self_wdc, name_wdc, age_wdc):
        self_wdc.name_wdc = name_wdc
        self_wdc.age_wdc = age_wdc


class Student_wdc(Person_wdc):
    def __init__(self_wdc, name_wdc, age_wdc, course_wdc):
        super().__init__(name_wdc, age_wdc)
        self_wdc.course_wdc = course_wdc

    def display_student_wdc(self_wdc):
        print("Name:", self_wdc.name_wdc)
        print("Age:", self_wdc.age_wdc)
        print("Course:", self_wdc.course_wdc)


student1_wdc = Student_wdc("Warren", 20, "BSIS")
student1_wdc.display_student_wdc()


#Warren Need 100GRADES