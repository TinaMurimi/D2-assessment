import numpy as np
from collusion_resolution import open_addressing


def hashing_midsquare(hash_table, key_value, skip=False):
    print()
    print(key_value)
    print('----')

    size = hash_table.size
    slot = 0

    print(f'size: {size}')

    if str(key_value).isdigit():
        # Square the element
        square = str(key_value**2)
        l = len(square)

        print(f'l//2: {l//2}')
        print(f'square: {square}')

        # Select the middle numbers
        if l % 2 == 0:
            mid_values = square[(l//2)-1] + square[(l//2)]

            print(f'1. mid_values: {mid_values}')
            slot = int(mid_values) % size
        elif l % 2 == 1:
            mid_values = square[(l//2)]

            print(f'2. mid_values: {mid_values}')
            slot = int(mid_values)
    else:
        """
        Hashing characters
        """
        l = len(key_value)
        print(f'l: {l}')
        total = 0
        for i in range(0, l-1):
            total += ord(key_value[i])

        slot = total % size

    return slot

    # # Check for collusion and resolve
    # resolved_slot = open_addressing(hash_table, slot, skip=skip)
    # hash_table[resolved_slot] = element


def quadratic_probing(hash_table, index=0):
    """
    Instead of using a constant “skip” value, we use a rehash function
    that increments the hash value by 1, 3, 5, 7, 9, and so on.
    This means that if the first hash value is h, the successive values
    are h+1, h+4, h+9, h+16, and so on. In other words, quadratic probing
    uses a skip consisting of successive perfect squares.
    """
    # l = len(elements)

    # # Create an array
    # # It is often suggested that the table size be a prime number
    # hash_table = np.repeat(None, size)

    size = hash_table.size

    first_hash_value = index

    if index > size:
        index = 0

    print(f'index: {index}, size: {size}')
    print('--------')

    # print(list(range(index, l-1)) + list(range(0, index)))
    # for i in list(range(index, l-1)) + list(range(0, index)):
    #     print(i)

    iterations = 0
    found = False

    skip = 0
    while not found :

        print('_________________________')
        print(f'size: {size}, index: {index}, iterations: {iterations}')
        print('_________________________')
        print(f'hash_table[index]: {hash_table[index]}')

        # if skip >= size or index >= size:
        #     return None

        if hash_table[index] is None:
            print(f'hash_table[index] is None: {hash_table[index] is None}')
            found = True
            return int(index)
        else:
            # for i in range(1, size-index):
            if first_hash_value == size-1:
                skip -= 1
            else:
                skip += 1

            index += skip**skip
            index = int(index)

            if(skip < 0 or index < 0) or (skip >= size or index >= size):
                return None
            print(f'2. index: {index}, skip: {skip}')
    #     print('--------')
        
    #         print(hash_table)
    # print(f'while| skip: {skip}')
    # print(f'while| index: {index}, skip: {skip}')
    # return None
    # else:
    #     print(f'else| skip: {skip}')
    #     print(f'else| index: {index}, skip: {skip}')
    #     return index

            # print(f'index += i**i: {index}')
            # print(f'index > size: {index > size}')

            # if skip > size or index > size:
            #     skip = 0
            #     index = 0
                # break

    #     index += skip**skip

    #     print(f'2. index: {index}, skip: {skip}')
    #     print('--------')

    #     # if index > size:
    #     #     index = 0

    #     iterations += 1
    #     if iterations >= 20:
    #         break

    # if not found:
    #     print(f'first_hash_value: {first_hash_value}')
    #     first_hash_value =+ 1
    #     quadratic_probing(hash_table=hash_table, index=first_hash_value)

    #         # quadratic_probing(hash_table=hash_table, index=index)

    # print(hash_table)
    # return index

    # print(f'completed')

    # iterations += 1

    # if iterations > size:
    #     raise Exception('TESTING....')

    # quadratic_probing(key_value, size, index)

    # iterations += 1

    # if iterations > size:
    #     return



# Create an array
# It is often suggested that the table size be a prime number
# size = 16
# size = 17
# size = 23
size = 64
hash_table = np.repeat(None, size)

elements = [54, 45, 82, 26, 93, 94, 50, 17, 33, 77, 31, 44, 55, 20, 30]
# elements = [54, 45, 82]
print(elements)

# for element in elements:
#     slot = hashing_midsquare(hash_table, element, 3)

# print(hash_table)

# Get first hash value
first_hash_value = hashing_midsquare(hash_table, elements[0])

print(f'\n\nfirst_hash_value: {first_hash_value}')
print('Hashing elements....')
for element in elements:
    print(f'\n\nelement: {element}')
    resolved_slot = quadratic_probing(
        hash_table=hash_table, index=first_hash_value)
    # break

    
    print(f'...resolved_slot: {resolved_slot}')
    # print(hash_table)

    if resolved_slot is not None:
        hash_table[resolved_slot] = element
    print(hash_table)

    # print(hash_table)
