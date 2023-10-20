# import pandas as pd

# # Builds a class of type DataFrame
# # df holds a DataFrame object
# # when I create a new object and save it to a variable
# # I say that I have "instantiated" that object
# df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})


# if __name__ == "__main__":

#     # Variables that form part of an "object"
#     # are called "attributes"
#     print(df.shape)
#     print(df.dtypes)
#     print(df.index)
#     print(df.columns)

#     # Functions that form part of an "object"
#     # are called "methods"
#     print(df.head())
#     print(df.describe())
#     print(df.isnull().sum())

#     # a method associated with a Pandas "series" object
#     # aka "columns"
#     # which lives inside of a DataFrame
#     print(df['a'].value_counts())

class Wallet:

    # first thing to run when we make a new class
    # outline required user-previded input values here
    # parameters with default values assigned are *optional*
    # passing in a value to a default optional parameter
    # overrides its value
    def __init__(self, initial_amount=0):
        # save the user-provided initial_amount as an attribute
        # self refers to whatever object I'm working with
        self.balance = initial_amount

    # spend cash METHOD
    def spend_cash(self, amount):
        if self.balance < amount:
            return "Remaining balance: 0"
        else:
            self.balance = self.balance - amount
            return f"Remaining balance: {self.balance}"

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f"New balance of: {self.balance}"

    # __repr__ method
    # changes how the "object looks when it is printed out
    # the presence of the self keyword allows me to access or
    # modify class attrivutes within this function
    def __repr__(self):
        return f"Wallet with balance of: ${self.balance}"

#if __name__ == "__main__":
    # adding .balance behind wallet1 in the print function
    # will print only 100 instead of the whole statement
    # print(wallet1.add_cash(60))
    # print(wallet1.spend_cash(180))
    # print(wallet1.spend_cash(120))
    # print(wallet1.balance)


