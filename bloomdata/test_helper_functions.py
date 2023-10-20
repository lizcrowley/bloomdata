import bloomdata.helper_functions as hf

adj = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
noun = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']


"""
My random_phrase function has no parameters so I cannot pass anything in
to break the code.
"""

def test_random_phrase():
    assert type(hf.random_phrase()) == str