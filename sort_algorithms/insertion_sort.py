def insertion_sort(elements):
    iterations = 0

    l = len(elements)

    # We begin by assuming that a list with one item (position 0)
    # is already sorted
    for i in range(1, l):
        print(f'\ni: {i}')
        print('----')

        curr = elements[i]
        pos = i

        # print(f'pos: {pos}')
        # print(f'1, elements[pos]: {elements[pos]}')
        
        # print(f'{elements[pos-1]} > {curr}')

        # print(f'pos: {pos}')

        # print(elements)

        while pos > 0 and elements[pos-1] > curr:
            # print(f'1, elements[pos]: {elements[pos]}')
            print(f'pos: {pos}')
            print(f'{elements[pos-1]} > {curr}')
            elements[pos] = elements[pos-1]
            pos -= 1

        elements[pos] = curr

        # print(f'2, elements[pos]: {elements[pos]}')

        # print(elements)

        iterations += 1

    print(f'\nTotal comparisons: {iterations}\n')


elements = [20, 545, 26, 26, 76, 54, 31, 44]
elements = [20, 3, 545, 26, 26, 76, 54, 31, 44]
insertion_sort(elements)
