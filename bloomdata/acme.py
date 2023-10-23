'''This class is meant to create products with certain variables for
a practice example of working at the Acme Corporation.'''
import random

'''Product class creates product information and determines certain
factors of given product.'''
class Product:

    '''Initialize Product class with given variables: name is name of the 
    product, identifier is a random integer between 1000000 and 9999999, price
    is defaulted at 10, weight is defaulted at 20, and flammability is 
    defaulted at 0.5.'''
    def __init__(self, name, identifier=random.randint(1000000, 9999999), 
                 price=10, weight=20, flammability=0.5):
        self.name = name
        self.identifier = identifier
        self.price = price
        self.weight = weight
        self.flammability = flammability

    '''Stealability method calculates the price devided by the weight and returns
    string based on how likely product will be to steal.'''
    def stealability(self):
        calc = self.price / self.weight
        if calc < 0.5:
            return "Not so stealable..."
        if calc < 1.0 and (calc > 0.5 or calc == 0.5):
            return "Kinda stealable."
        return "Very stealable!"
    
    '''Explode method calculates flammability multiplied by weight and returns
    string based on how likely the product is to explode.'''
    def explode(self):
        expl = self.flammability * self.weight
        if expl < 10:
            return "...fizzle."
        if expl < 50 and (expl > 10 or expl == 10):
            return "...boom!"
        return "...BABOOM!!"

    def __repr__(self):
        prod_list = self.name, self.identifier, self.price, self.weight, self.flammability
        return f'{prod_list}'
        #return f'''{self.name} has the identifier {self.identifier} with a price of {self.price}, 
                    #a weight of {self.weight}, and a flammability value of {self.flammability}.'''

'''BoxingGlove is a class that inherits variables from the Product class but includes
a few new methods for the child class.'''
class BoxingGlove(Product):

    '''Initializing the BoxingGlove class variables the same as the Product class but weight is
    defaulted at 10 instead of 20.'''
    def __init__(self, name, identifier=random.randint(1000000, 9999999)
                 , price=10, weight=10, flammability=0.5):
        super().__init__(name, identifier, price, weight, flammability)

    '''Explode method now only returns the phrase "...it's a glove."'''
    def explode(self):
        return "...it's a glove."
    
    '''Punch method returns a string based on what the weight of the BoxingGlove is.'''
    def punch(self):
        if self.weight < 5:
            return "That tickles."
        if self.weight < 15 and (self.weight > 5 or self.weight == 5):
            return "Hey that hurt!"
        return "OUCH!"

# if __name__ == "__main__":
#     prod = Product('A Cool Toy')
#     box = BoxingGlove('Punchy the Third')

#     print(Product)
#     print(BoxingGlove)

#     print(f'BoxingGlove sepcs: {box.name}')
#     print(f'identifier: {box.identifier}')
#     print(f'price: {box.price}')
#     print(f'weight: {box.weight}')
#     print(f'flammability: {box.flammability}')
#     print(f'explode: {box.explode()}')
#     print(f'punch: {box.punch()}')

#     print(f'Product sepcs: {prod.name}')
#     print(f'identifier: {prod.identifier}')
#     print(f'price: {prod.price}')
#     print(f'weight: {prod.weight}')
#     print(f'flammability: {prod.flammability}')
#     print(f'stealability: {prod.stealability()}')
#     print(f'explode: {prod.explode()}')