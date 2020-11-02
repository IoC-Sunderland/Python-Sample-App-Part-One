""" Vince's Vehicle:

This system allows the user to rent different types of vehicles

"""

# Inherits from Object automatically
class Vehicle:
    def __init__(self, colour, weight, brand):

        self.colour = colour
        self.weight = weight
        self.brand = brand

    def __str__(self):
        vehicle_description = f"\nColour: {self.colour}\n" \
                              f"Weight: {self.weight}\n" \
                              f"Brand: {self.brand}"

        return vehicle_description

    def __repr__(self):
        repr_output = f'{self.__class__.__name__}(' \
                      f'colour="{self.colour}", ' \
                      f'weight={self.weight}, ' \
                      f'brand="{self.brand}")'

        return repr_output



class Car(Vehicle):
    pass


class Boat(Vehicle):
    
    def __init__(self, colour, weight, brand, motor_type):
        super().__init__(colour, weight, brand)
        self.motor_type = motor_type


    def __str__(self):

        boat_description = f"{super().__str__()}\n" \
                           f"Motor Type: {self.motor_type}"

        return boat_description


    def __repr__(self):
         
        boat_repr = f"{super().__repr__()}\n" \
                     f"Motor Type: {self.motor_type}"
        
        return boat_repr


class Plane(Vehicle):
    pass


class RentalLog:
    pass


class RentalRates:
    pass


class AdminUser:
    pass


class User:
    pass


v1 = Vehicle('Red', 1000, 'Unknown')
c1 = Car('Blue', 1113, 'Ford')
b1 = Boat('White', 3000, "Billy's Boats", "Outboard")
p1 = Plane('White', 5000, "Paula's Planes")

