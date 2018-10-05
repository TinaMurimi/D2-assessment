def shell_sort(elements):
    sublistcount = len(elements)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(elements, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", elements)

        sublistcount = sublistcount // 2


def gapInsertionSort(elements, start, gap):
    for i in range(start+gap, len(elements), gap):

        currentvalue = elements[i]
        position = i

        while position >= gap and elements[position-gap] > currentvalue:
            elements[position] = elements[position-gap]
            position = position-gap

        elements[position] = currentvalue


elements = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(elements)
print(elements)
