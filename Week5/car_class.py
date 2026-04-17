class Car:
    def __init__(self, car_brand, car_model, car_year):
        self.car_brand = car_brand
        self.car_model = car_model
        self.car_year = car_year

    def display_car(self):
        print("Brand:", self.car_brand)
        print("Model:", self.car_model)
        print("Year:", self.car_year)


# Create an object
car1 = Car("BMW", "Supra", 2022)

# Display car information
car1.display_car()