'''
This file holds two classes: Vehicle and Convertible. 
They are parent and child class.
'''


class Vehicle:
    '''
    This is the class docstring.
    Imagine i want to list theses vehicles on Craigslist
    "Parent" class is the more generic of the two
    '''

    def __init__(self, make, model, color, year, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
    
    def honk(self):
        return "HOOOOOOOONK!"

    def drive(self, miles_driven):
        self.mileage = self.mileage + miles_driven
        return self.mileage

    def __repr__(self):
        return f"A {self.color} {self.year} {self.make} {self.model} with {self.mileage} miles."
    
if __name__ == "__main__":
    my_vehicle = Vehicle('Toyota', 'Camry', 'gray', 2015, 60000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)

    print(my_vehicle)


class Convertible(Vehicle):
    '''
    This is the class docstring.
    The more specific class is called the "child" class because it
    Inherits from the "Parent" class
    Convertible class inherits from Vehicle
    '''
    # any default parameters have to be listed at END of line
    # required parameters always come first and default come second
    def __init__(self, make, model, color, year, mileage, top_down=True):
        super().__init__(make, model, color, year, mileage)
        self.top_down = top_down

    def change_top_status(self):
        if self.top_down:
            self.top_down = False
            return "Top is now up!"
        else:
            self.top_down = True
            return "Top is now down!"

    def __repr__(self):
        return f'''A {self.color} {self.year} {self.make} {self.model} 
        convertible with {self.mileage} miles.'''
    

if __name__ == "__main__":
    my_vehicle = Convertible('Toyota', 'Camry', 'gray', 2015, 60000)

    print(my_vehicle.make)
    print(my_vehicle.mileage)

    print(my_vehicle.honk())
    print(my_vehicle.drive(1234))
    print(my_vehicle.mileage)

    print(my_vehicle)

    print(my_vehicle.top_down)
    print(my_vehicle.change_top_status)
    print(my_vehicle.top_down)