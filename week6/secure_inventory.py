class Product:
    def __init__(self, apd_name, apd_price, apd_quantity):
        # Private attributes with apd_ prefix
        self.__apd_name = apd_name
        self.__apd_price = apd_price
        self.__apd_quantity = apd_quantity

    def get_product_info(self):
        # Displays all private product details
        print(f"Product: {self.__apd_name}")
        print(f"Price: {self.__apd_price}")
        print(f"Quantity: {self.__apd_quantity}")

    def update_quantity(self, apd_new_quantity):
        # Logic to ensure quantity doesn't go below zero
        if apd_new_quantity >= 0:
            self.__apd_quantity = apd_new_quantity
        else:
            print("Error: Quantity cannot be negative.")

    def update_price(self, apd_new_price):
        # Logic to ensure price is valid
        if apd_new_price > 0:
            self.__apd_price = apd_new_price
        else:
            print("Error: Price must be greater than zero.")

# Creating an instance of Product
apd_product1 = Product("Laptop", 45000, 10)

# Displaying the initial info
apd_product1.get_product_info()