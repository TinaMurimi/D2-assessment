def merge_sort(elements):
    iterations = 0

    l = len(elements)
    if l > 1:
        mid = len(elements)//2
        lefthalf = elements[:mid]
        righthalf = elements[mid:]

        print(f'lefthalf: {lefthalf}')
        print(f'righthalf: {righthalf}')

        print('\n\nSorting left half')
        merge_sort(lefthalf)

        print('\n\nSorting right half')
        merge_sort(righthalf)

        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            print(f'\nLoop 1-- i: {i} j: {j} k: {k}')
            print('--------------')
            print(f'lefthalf: {lefthalf}')
            print(f'righthalf: {righthalf}')

            print(f'1. elements: {elements}')
            if lefthalf[i] < righthalf[j]:
                elements[k] = lefthalf[i]
                i = i+1
            else:
                elements[k] = righthalf[j]
                j = j+1
            k = k+1

            print(f'2. elements: {elements}')

            iterations += 1

        while i < len(lefthalf):
            print(f'Loop 2-- i: {i} j: {j} k: {k}')
            print('--------------')
            print(f'lefthalf: {lefthalf}')
            print(f'righthalf: {righthalf}')

            print(f'1. elements: {elements}')
            elements[k] = lefthalf[i]
            i = i+1
            k = k+1

            print(f'2. elements: {elements}')

            iterations += 1

        while j < len(righthalf):
            print(f'Loop 3-- : {i} j: {j} k: {k}')
            print('--------------')
            print(f'lefthalf: {lefthalf}')
            print(f'righthalf: {righthalf}')

            print(f'1. elements: {elements}')
            elements[k] = righthalf[j]
            j = j+1
            k = k+1

            print(f'2. elements: {elements}')

            iterations += 1

        print("Merging ", elements)

        # print(f'Total comparisons: {iterations}')


elements = [123, 120, 87, 104, 909, 56, 545, 26, 26, 76, 54, 31, 44, 98, 678]
merge_sort(elements)
