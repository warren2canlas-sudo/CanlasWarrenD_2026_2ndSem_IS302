class Person:
    def __init__(self, person_name, person_age):
        self.person_name = person_name
        self.person_age = person_age

    def display_info(self):
        print("Name:", self.person_name)
        print("Age:", self.person_age)


# Create an object
person1 = Person("Juan Dela Cruz", 21)

# Call the method
person1.display_info()