import os
from random import randint


# e
EPSILONS = [
    0.2,
    0.3,
    0.5
]

# c
CAPACITIES = [
    500,
    1000,
    2000,
]

# v
ELEMENTS_AMOUNTS = [
    10,
    50,
    75,
    100,
]

MAX_RANDOM_VALUE = 100

def MAX_RANDOM_WEIGHT(capacity, elements_amount):
    return (capacity * 3) // elements_amount


def generate_tests():
    path = os.path.dirname(os.path.abspath(__file__))

    for epsilon in EPSILONS:
        epsilon_str = str(epsilon)[0] + "." + str(epsilon)[2:].ljust(4, '0')
        try:
            os.mkdir(os.path.join(path, f"e{epsilon_str}"))
        except FileExistsError:
            pass

    for epsilon in EPSILONS:
        epsilon_str = str(epsilon)[0] + "." + str(epsilon)[2:].ljust(4, '0')

        for capacity in CAPACITIES:
            for elements_amount in ELEMENTS_AMOUNTS:
                filename = f'test_e{epsilon_str}_c{capacity}_v{str(elements_amount)}.csv'
                csvpath = os.path.join(path, f"e{epsilon_str}", filename)
                with open(csvpath, 'x') as f:
                    f.write(f'{epsilon}\n')
                    f.write(f'{capacity}\n')
                    f.write(f'{elements_amount}\n')
                    for i in range(elements_amount):
                        weight = randint(1, MAX_RANDOM_WEIGHT(capacity, elements_amount))
                        value = randint(0, MAX_RANDOM_VALUE)
                        f.write(f'{weight}, {value}\n')


generate_tests()
