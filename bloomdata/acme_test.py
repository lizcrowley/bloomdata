'''I had to run python -m pytest acme_test.py for this to run properly'''
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS
import pytest


@pytest.fixture
def prod_init():
    '''pytest fixture to clean up code'''
    return Product('Test Product')


def test_default_product_price():
    '''Testing to ensure defualt price is 10'''
    prod = prod_init()
    assert prod.price == 10


def test_stealability():
    '''Testing to ensure stealability() results in a str'''
    assert isinstance(prod_init().stealability(), str)


def test_explode():
    '''Testing to ensure explode() results in a str'''
    assert isinstance(prod_init().explode(), str)


def test_attr():
    '''Testing to ensure Product().price is an int'''
    price = prod_init().price
    assert isinstance(price, int)


def test_gen_prod():
    '''Testing to ensure default list length is 30'''
    prod = generate_products()
    assert len(prod) == 30
    assert isinstance(ADJECTIVES[0], str)
    assert isinstance(NOUNS[0], str)
