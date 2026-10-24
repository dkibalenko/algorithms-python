# swap array


# def func(array, i, j):
#     item_1, item_2 = array[i], array[j]
#     array[i] = item_2
#     array[j] = item_1


def swap(array: list, i: int, j: int) -> None:
    """Swap elements at indices i and j in place."""
    array[i], array[j] = array[j], array[i]


array = [1, 2, 3, 4, 5]

swap(array, 1, 2)
print(array)
