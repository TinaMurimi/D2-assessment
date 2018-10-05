def hashing_folding(key_value, size):
    key_value = str(key_value)
    l = len(key_value)

    total = 0
    # Group the key value in 2s and sum them
    for i in range(0, l-1, 2):
        value = key_value[i]+key_value[i+1]
        total += int(value)

    print()
    print(key_value)
    print('---------')
    print(f'total: {total}')
    print(f'slot: {total % size}')

    return total % size


def hashing_folding_extended(key_value, size, interchange=True):
    """
    Some folding methods go one step further and reverse every
    other piece before the addition.
    """

    key_value = str(key_value)
    l = len(key_value)

    change = 0

    total = 0
    iterations = 0
    # Group the key value in 2s and sum them
    for i in range(0, l-1, 2):
        value = key_value[i]+key_value[i+1]

        if iterations and interchange and iterations % 2:
            value = key_value[i+1]+key_value[i]
        else:
            value = key_value[i]+key_value[i+1]

        total += int(value)
        iterations += 1

    print()
    print(key_value)
    print('---------')
    print(f'total: {total}')
    print(f'slot: {total % size}')

    return total % size


import numpy as np

# Create an array
size = 11
hash_table = np.repeat(None, size)

elements = [4365554601, 75029752025, 5493037502,
            745728422844, 57592852954, 2345, 23456]

for element in elements:
    slot = hashing_folding_extended(element, size=size)
    if not hash_table[slot] is None:
        print(f'Collision at slot {slot}')
        # raise ValueError(f'Collision at slot {slot}')
    else:
        hash_table[slot] = element

print(hash_table)
