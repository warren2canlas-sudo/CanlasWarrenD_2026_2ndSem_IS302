class Employee_wdc:
    def __init__(self_wdc, name_wdc, salary_wdc):
        self_wdc.name_wdc = name_wdc
        self_wdc.salary_wdc = salary_wdc


class Manager_wdc(Employee_wdc):
    def __init__(self_wdc, name_wdc, salary_wdc, department_wdc):
        super().__init__(name_wdc, salary_wdc)
        self_wdc.department_wdc = department_wdc

    def display_manager_wdc(self_wdc):
        print("Name:", self_wdc.name_wdc)
        print("Salary:", self_wdc.salary_wdc)
        print("Department:", self_wdc.department_wdc)


manager1_wdc = Manager_wdc("Warren", 50000, "IS")
manager1_wdc.display_manager_wdc()