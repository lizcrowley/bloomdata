'''Must import classes from acme.py and random for variable input selection.'''
import re
import random
from acme import Product

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Diguise', 'Mousetrap', '???']

'''The following 5 functions are meant to supplement the core functions
of this report.'''


def rand_phrase():
    '''* rand_phrase() -> generates a random phrase with an adjective and
    noun from the lists above.'''
    lis1 = random.randint(0, 4)
    lis2 = random.randint(0, 4)
    return f'{ADJECTIVES[lis1]} {NOUNS[lis2]}'


def rand_price():
    '''* rand_price() -> generates a random price from 5 to 100'''
    return random.randint(5, 100)


def rand_weight():
    '''* rand_weight() -> generates a random weight from 5 to 100'''
    return random.randint(5, 100)


def rand_flam():
    '''* rand_flam() -> generates a random float from 0 to 2.5 rounded to
    1 floating point'''
    flam = random.uniform(0, 2.5)
    return round(flam, 1)


def gen_prod():
    '''* gen_prod() -> generates random output for the Product class'''
    ident = random.randint(1000000, 9999999)
    prod = (Product(name=rand_phrase()).name,
            rand_price(),
            rand_weight(),
            rand_flam(),
            ident)
    return prod


def generate_products(num_products=30):
    '''* generate_products() -> This function is defaulted at a total of 30
    items. This function generates a list of num_products items randomly
    generated from the gen_prod function.'''
    prod_array = []
    arr = []
    count = num_products
    while count > 0:
        ident = random.randint(1000000, 9999999)
        prod_array = [Product(name=rand_phrase(),
                              price=rand_price(),
                              weight=rand_weight(),
                              flammability=rand_flam(),
                              identifier=ident)]
        arr += prod_array
        count -= 1
    return arr


def inventory_report(product_list):
    '''* inventory_report() -> This function creates a set of items based on
    calculations made on the randomly generated list from generate_products.
    The list contains the number of unique product names, average price,
    average weight, and average flammability from the generate_products list.
    '''
    result = [0, 0, 0, 0]

    check_name = str(product_list)
    name = re.findall("'([^']*)'", check_name)
    num = 0
    my_set = set(name)
    for _ in my_set:
        num += 1
    result[0] = num

    avg_p = 0
    for i in range(len(product_list)):
        avg_p += product_list[i].price
    result[1] = avg_p / len(product_list)

    avg_w = 0
    for i in range(len(product_list)):
        avg_w += product_list[i].weight
    result[2] = avg_w / len(product_list)

    avg_f = 0
    for i in range(len(product_list)):
        avg_f += product_list[i].flammability
    result[3] = avg_f / len(product_list)

    return result


if __name__ == "__main__":
    print(generate_products())
    print(inventory_report(generate_products()))
