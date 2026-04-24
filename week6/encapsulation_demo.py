class Person:
    def __init__(self, apd_name, apd_age):
        # Private attributes with apd_ prefix
        self.__apd_name = apd_name
        self.__apd_age = apd_age

    # Getter method for name
    def get_name(self):
        return self.__apd_name

    # Getter method for age
    def get_age(self):
        return self.__apd_age

# Creating an instance of Person
# 'p1' becomes 'apd_p1' to stay consistent
apd_p1 = Person("Maria", 20)

# Accessing data via getters
print(f"Name: {apd_p1.get_name()}")
print(f"Age: {apd_p1.get_age()}")

#warren