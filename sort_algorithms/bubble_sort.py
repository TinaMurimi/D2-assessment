"""
- Works by repeatedly stepping through the list to be sorted, comparing each pair of adjacent items and swapping them if they are in the wrong order. If we have a total of n elements, we need to repeat the process (n-1) times. 
- Can be modified to stop early if it finds that the list has become sorted. Therefore, instead of n(n-1) comparisons, we have n(n-1)/2 comparisons.
- Not practical when n is large.
Performance: Worst Case O(n2), Best Case O(n)
"""

def bubble_sort(elements):
    l = len(elements)-1

    iterations = 0
    for k in range(l, 0, -1):
    # for k in range(l):
        print(f'\nk: {k}')
        print('----')
        for i in range(k):
        # for i in range(l):
            print(f'i: {i}')
            j = i + 1
            temp = elements[i]
            if elements[i] > elements[j]:
                elements[i] = elements[j]
                elements[j] = temp

            iterations += 1


            print(elements)
    print(iterations)

    return elements


elements = [100, 26, 93, 17, 77, 31, 44]
bubble_sort(elements)


# Modified to allow sorting to stop if the list is already sorted
def modified_bubble_sort(elements):
    l = len(elements) -1
    exchange = True

    while exchange and l > 0:
        print(f'\nl: {l}')
        print('--------------')
        for i in range(l):
            print(f'i: {i}')
            j = i + 1

            exchange = True
            temp = elements[i]
            if elements[i] > elements[j]:
                elements[i] = elements[j]
                elements[j] = temp

            print(elements)

        l -= 1

    return elements


elements = [54, 26, 93, 17, 77, 31, 44]
elements = [54, 44, 45, 46, 47, 49, 100]
elements = [44, 45, 46, 47, 49, 54, 100]
# modified_bubble_sort(elements)
# print(modified_bubble_sort(elements))
