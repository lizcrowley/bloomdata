'''I had to run python -m pytest acme_test.py for this to run properly'''
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
import pytest

'''Testing to ensure defualt price is 10'''
def test_default_product_price():
    '''Test default price being 10.'''
    prod = Product('Test Product')
    assert prod.price == 10

'''Testing to ensure stealability() results in a str'''
def test_stealability():
    assert type(Product('Test Product').stealability()) == str

'''Testing to ensure explode() results in a str'''
def test_explode():
    assert type(Product('Test Product').explode()) == str

'''Testing to ensure Product().price is an int'''
def test_attr():
    price = Product('Test Product').price
    assert type(Product('Test Product').price) == int

'''Testing to ensure default list length is 30'''
def test_gen_prod():
    prod = generate_products()
    assert len(prod) == 30