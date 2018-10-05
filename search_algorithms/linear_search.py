def linear_search(elements, target):
    found = False
    for index, value in enumerate(elements):
        print(f'{value} == {target}')
        if value == target:
            # found = True
            # break

            return index

    # return found
    return -1

    
elements = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(linear_search(elements, 17))
print(linear_search(elements, 45))