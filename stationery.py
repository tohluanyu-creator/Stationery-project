#Import is not needed here as this is a separate class file

#Stationery class to calculate total price of each item
class Stationery:
    #Initialise the stationery item with name, quantity and price
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
    #Function to calculate and return the total price
    def calculate_total(self):
        return self.quantity * self.price #multiply quantity by price