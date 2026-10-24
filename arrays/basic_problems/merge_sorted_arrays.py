
def merge_sorted_arrays(array1: list[int], array2: list[int]) -> list[int]:
    # basic input validation
    if not array1:
        return array2
    if not array2:
        return array1

    # [0, 3, 4, 31] and [4, 6, 30]
    bucket = []  # merged result

    # Start with the first elements from each array
    # i = j = 0
    # arr1_item = array1[i]
    # arr2_item = array2[j]
    # i += 1
    # j += 1

    # take inital elements for comparison & track the current items comparing from each array
    arr1_item = array1[0]
    arr2_item = array2[0]

    # pointers at 1 because we’ve already “taken” the first element for comparison
    i = 1  # track array1
    j = 1  # track array2

    # main merge loop. Merge until one array is exhausted
    while True:
        print(f"Array items: {arr1_item}; {arr2_item}")

        if arr1_item <= arr2_item:
            bucket.append(arr1_item)

            # make sure array has items before trying to grab it
            if i < len(array1):
                # re-assign next item for comparison & advance pointer
                arr1_item = array1[i]
                i += 1
            else:
                # when the array runs out, we immediately append the current item from 
                # the other array, then bulk-extend the rest — no risk of IndexError
                bucket.append(arr2_item)  # add current array2 item
                bucket.extend(array2[j:])  # add all array2 items after the current, as 'j' points to the next item
                break  # complete
        else:
            bucket.append(arr2_item)

            if j < len(array2):
                arr2_item = array2[j]
                j += 1
            else:
                # array2 is exhausted — drop in the rest of array1 (including current)
                bucket.append(arr1_item)
                bucket.extend(array1[i:])
                break

    return bucket


def merge_sorted_arrays2(array1: list[int], array2: list[int]) -> list[int]:
    if not array1:
        return array2
    if not array2:
        return array1
    
    bucket = []
    i = j = 0

    # Merge until one array is exhausted
    while i < len(array1) and j < len(array2):

        if array1[i] <= array2[j]:
            bucket.append(array1[i])
            i += 1
        else:
            bucket.append(array2[j])
            j += 1

    # Append leftovers (only one of these will run)
    bucket.extend(array1[i:])
    bucket.extend(array2[j:])

    return bucket

print(merge_sorted_arrays2([0, 3, 4, 31], [4, 6, 30]))



