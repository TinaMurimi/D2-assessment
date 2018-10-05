"""
- An in-pace comparison sort that improves on the bubble sort by making only one exchange for every pass through the list. It selects the next smallest element and swaps it into the right place
- Not practical when n is large.
Performance: Worst Case O(n2), Best Case O(n2)
"""


def selection_sort(elements):
    iterations = 0

    l = len(elements)
    for i in range(0, l-1, 1):
        min_pos = i

        print(f'\ni: {i}')
        print('----')

        # Find the smallest number first
        for j in range(i, l, 1):
            if elements[j] < elements[min_pos]:
                min_pos = j

            iterations += 1

        print(f'min_pos: {min_pos}')
        print(f'elements[i]: {elements[i]}, '
              f'elements[min_pos]: {elements[min_pos]}')

        print(elements)

        if min_pos != i:
            temp = elements[i]
            elements[i] = elements[min_pos]
            elements[min_pos] = temp

            print(elements)

    print(f'\nTotal comparisons: {iterations}')


elements = [20, 545, 26, 26, 76, 54, 31, 44]
selection_sort(elements)


def selection_sort(elements):
    iterations = 0

    l = len(elements)
    for i in range(l-1, 0, -1):
        max_pos = 0
        for j in range(1, i+1):
            if elements[j] > elements[max_pos]:
                max_pos = j

            iterations += 1

        temp = elements[i]
        elements[i] = elements[max_pos]
        elements[max_pos] = temp

    print(f'\nTotal comparisons: {iterations}')


# elements = [100, 545, 26, 93, 76, 77, 31, 44]
# selection_sort(elements)
