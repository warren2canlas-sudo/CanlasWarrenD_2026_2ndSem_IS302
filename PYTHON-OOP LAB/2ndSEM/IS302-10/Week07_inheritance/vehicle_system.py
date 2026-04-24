class Vehicle_wdc:
    def __init__(self_wdc, brand_wdc, model_wdc):
        self_wdc.brand_wdc = brand_wdc
        self_wdc.model_wdc = model_wdc


class Car_wdc(Vehicle_wdc):
    def __init__(self_wdc, brand_wdc, model_wdc, year_wdc):
        super().__init__(brand_wdc, model_wdc)
        self_wdc.year_wdc = year_wdc

    def display_car_wdc(self_wdc):
        print(self_wdc.brand_wdc, self_wdc.model_wdc, self_wdc.year_wdc)


car1_wdc = Car_wdc("Toyota", "Warren", 2022)
car1_wdc.display_car_wdc()

#Warren Need 100Grades