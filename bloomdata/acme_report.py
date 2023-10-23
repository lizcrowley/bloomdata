'''Must import classes from acme.py and random for variable input selection.'''
from acme import Product
import random
import re

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Diguise', 'Mousetrap', '???']

'''The following 5 functions are meant to supplement the core functions
of this report.'''

'''* rand_phrase() -> generates a random phrase with an adjective and noun from the
lists above.'''
def rand_phrase():
    lis1 = random.randint(0, 4)
    lis2 = random.randint(0, 4)
    return f'{ADJECTIVES[lis1]} {NOUNS[lis2]}'

'''* rand_price() -> generates a random price from 5 to 100'''
def rand_price():
    return random.randint(5, 100)

'''* rand_weight() -> generates a random weight from 5 to 100'''
def rand_weight():
    return random.randint(5, 100)

'''* rand_flam() -> generates a random float from 0 to 2.5 rounded to 1 floating point'''
def rand_flam():
    flam = random.uniform(0, 2.5)
    return round(flam, 1)

'''* gen_prod() -> generates random output for the Product class'''
def gen_prod():
    ident = random.randint(1000000, 9999999)
    prod = Product(name=rand_phrase()).name, rand_price(), rand_weight(), rand_flam(), ident
    return prod

'''* generate_products() -> This function is defaulted at a total of 30 items. This function
generates a list of num_products items randomly generated from the gen_prod function.
'''
def generate_products(num_products=30):
    prod_array = []
    for _ in range(num_products):
        prod_array += [gen_prod()]
    return prod_array

'''* inventory_report() -> This function creates a set of items based on calculations made on the 
randomly generated list from generate_products. The list contains the number of unique product
names, average price, average weight, and average flammability from the generate_products list.'''
def inventory_report(product_list=generate_products()):
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
        avg_p += product_list[i][1]
    result[1] = round(avg_p / len(product_list), 1)

    avg_w = 0
    for i in range(len(product_list)):
        avg_w += product_list[i][2]
    result[2] = avg_w / len(product_list)

    avg_f = 0
    for i in range(len(product_list)):
        avg_f += product_list[i][3]
    result[3] = avg_f / len(product_list)
    
    return result

if __name__ == "__main__":
    print(generate_products())
    print(inventory_report())