class Employee:
    def __init__(self, apd_name):
        # Private attributes with apd_ prefix
        self.__apd_name = apd_name
        self.__wai_salary = 0

    # Setter method: used to update the salary with validation logic
    def set_salary(self, apd_salary):
        if apd_salary > 0:
            self.__wai_salary = apd_salary
        else:
            print("Error: Salary must be a positive amount.")

    # Getter method: used to safely retrieve the salary
    def get_salary(self):
        return self.__apd_salary

# Creating an instance of Employee
apd_emp = Employee("wai")

# Setting the salary using the setter method
apd_emp.set_salary(30000)

# Displaying the result
print(f"Employee: {apd_emp._Employee__apd_name}") # Internal access check (for demo)
print(f"Salary: {apd_emp.get_salary()}")