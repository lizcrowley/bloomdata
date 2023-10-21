import numpy as np

rng = np.random.default_rng()

def random_phrase():
    adj = ['blue', 'large', 'grainy', 'substantial', 'potent', 'thermonuclear']
    noun = ['food', 'house', 'tree', 'bicycle', 'toupee', 'phone']

    pick = rng.integers(low=0, high=6, size=2)

    return f'{adj[pick[0]]}'+f' {noun[pick[1]]}'

def random_float(min_val, max_val):
    ran = rng.uniform(low=min_val, high=max_val, size=None)

    return ran

def random_bowling_score():
    score = rng.integers(low=0, high=301, size=None)

    return score

def silly_tuple():
    silly = (random_phrase(), random_float(10, 20), random_bowling_score())

    return silly

def silly_tuple_list(num_tuples):
    lis = []
    count = num_tuples

    while count > 0:
        lis.append(silly_tuple())
        count -= 1
    
    return lis

if __name__ == '__main__':
    pass
    # print(silly_tuple_list(3))
