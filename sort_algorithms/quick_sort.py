"""
- Selects a "pivot value" which assists with splitting the list. Next, perform a parttition operation and reorder the list so that all the elements which are less than the pivot value are on the left side of the pivot value and all the greater elements are on the the right side of the pivot value. Equal values go either way.
Performance: Worst Case O(n*n), Best Case O(n log n)
"""


def quickSort(elements):
    quickSortHelper(elements, 0, len(elements)-1)


def quickSortHelper(elements, first, last):
    if first < last:

        splitpoint = partition(elements, first, last)

        quickSortHelper(elements, first, splitpoint-1)
        quickSortHelper(elements, splitpoint+1, last)


def partition(elements, first, last):
    pivotvalue = elements[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and elements[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while elements[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = elements[leftmark]
            elements[leftmark] = elements[rightmark]
            elements[rightmark] = temp

    temp = elements[first]
    elements[first] = elements[rightmark]
    elements[rightmark] = temp

    return rightmark


elements = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(elements)
print(elements)
