"""
Searches through sorted lists using divide and conquer strategy.
Starts by examining the middle element. If the middle element is equal to the
element we are searching for, we are done. Else, if the element we are
searching for is is greater that  the middle item, we know the lower half
of the list as well as the middle element can be eliminated from
consideration. We repear the process for the upper half.
- Has time complexity of O(log n)
"""


def binary_search(elements, target):
    """
    Recursive binary search
    """
    if not len(elements):
        # return -1
        return False

    # Get mid_point
    m = len(elements)//2
    midpoint = elements[m]

    # print()
    # print(f'elements[{m}]: {midpoint}')

    less = elements[0:m]
    more = elements[m+1:]

    # print(f'less: {less}')
    # print(f'more: {more}')

    if midpoint == target:
        return True
    elif midpoint < target:
        return binary_search(more, target)
    else:
        return binary_search(less, target)

    # return found
    # return -1
    return False


# elements = [17, 20, 26, 31, 44, 54, 55, 77, 93]
# print(binary_search(elements, 31))
# print(binary_search(elements, 45))


def binary_search(elements, target):
    l = len(elements)
    if not l:
        return -1

    first = 0
    last = l-2
    while True:
        m = (first + last)//2
        midpoint = elements[m]

        # print(f'\nelements[{m}]: {midpoint}')
        # print(f'first: {first}')
        # print(f'last: {last}')
        if midpoint == target:
            return m
        elif midpoint < target:
            first += 1
        else:
            last -= 1

        if first > last:
            return -1


elements = [17, 20, 26, 31, 44, 54, 55, 77, 93]
print(binary_search(elements, 77))
print(binary_search(elements, 45))
