import random

def try_me():
    acronyme = [
        'ATM', 'BBBJ', 'BBFS', 'BBJTCNQNS', 'BLS', 'CIF', 'DATO', 'DP', 'FBSM',
        'MSOG', 'OWO', 'RPG', 'SOMF',
    ]
    i = random.randint(0, len(acronyme))
    return acronyme[i]

if __name__ == "__main__":
    print(try_me())
