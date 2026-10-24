def find_smallest(array):
    smallest = array[0]  # store the smallest value
    smallest_index = 0   # store the index of the smallest value

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i

    return smallest_index


# now you can use this function to write selection sort
def selection_sort(array):
    new_array = []

    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))

    return new_array
