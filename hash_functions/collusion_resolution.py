def open_addressing(hash_table, index, skip=0):
    """
    Tries to find the next open slot or address in the hash table.
    By systematically visiting each slot one at a time, we are performing
    an open addressing technique called linear probing.
    """
    l = hash_table.size
    if not hash_table[index] is None:
        print(
            f'We will look at every {skip}st/nd/rd/th slot until we find one that is empty.')
        print(f'Collision at slot {index}')
        print(hash_table)
        if not skip:
            for i in list(range(index, l-1)) + list(range(0, index)):
                if hash_table[i] is None:
                    print(f'Alternative slot {i}')
                    return i
        else:
            iteration = 0
            while iteration < skip:
                print(list(range(index, l-1, skip)) +
                      list(range(0, index, skip)))
                for i in list(range(index, l-1, skip)) + list(range(0, index, skip)):
                    if hash_table[i] is None:
                        print(f'Alternative slot {i}')
                        return i
                    index += skip
                    iteration += 1
    return index


def quadratic_probing(elements, hash_table):
    """
    Instead of using a constant “skip” value, we use a rehash function
    that increments the hash value by 1, 3, 5, 7, 9, and so on.
    This means that if the first hash value is h, the successive values
    are h+1, h+4, h+9, h+16, and so on. In other words, quadratic probing
    uses a skip consisting of successive perfect squares.
    """
    # See implemetation in hashing_midsquare()
    pass

"""
Other collision resolution techniques include:
Chaining:  Allow each slot to hold a reference to a collection (or chain) of items
Double Hashing: Choose a second hash function to determine the location of the next slot.
"""