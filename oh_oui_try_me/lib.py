import random


def try_me():
    acronyme = [
        'ATM',
        'BBBJ',
        'BBFS',
        'BBJTCNQNS',
        'BLS',
        'CIF',
        'DATO',
        'DP',
        'FBSM',
        'MSOG',
        'OWO',
        'RPG',
        'SOMF',
    ]
    i = random.randint(0, len(acronyme)-1)
    print(acronyme[i])


if __name__ == "__main__":
    try_me()
