import time
import timeit
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper


def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


# @timer
def bubble_sort(nums: list[int]) -> list[int]:
    # outer loop to traverse the entire list
    # inner loop to compare 2 adjacent elements
    # swap them when needed
    # optimization:
    # stop early: no swaps in a pass - stop sorting
    # shrink the inner loop, since 'i' part is sorted

    # repeat passes through the list
    for i in range(len(nums)):
        swapped = False  # signal if no swaps done in a single pass

        # compare adjacent pairs
        for j in range(len(nums) - 1 - i):  # shrink inner loop
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        
        if not swapped:  # stop early
            break
    return nums


# print(bubble_sort(numbers))


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


@timer
def selection_sort(nums):
    # start with min as the first item
    # use 2 pointers - fast & slow, nested loop
    # scan unsorted portion for min item
    # keep 2 portion - sorted(left) & unsorted(rigth)
    # find smallest item - bubble it up to the beginning of the list
    # swap in-place

    for i in range(len(nums)):
        min_idx = i  # current min

        # find min in unsorted region(i + 1, n)
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j  # update min

        # swap min
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

# print(selection_sort(numbers))


# @timer
def insertion_sort_naive(nums):  # [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
    for i in range(1, len(nums)):
        j = i

        while j > 0 and nums[j] < nums[j - 1]:
            nums[j], nums[j - 1] = nums[j - 1], nums[j]
            j -= 1
    return nums



# print(insertion_sort_naive(numbers))


# @timer
def merge_sort(array: list[int]) -> list[int]:
    n = len(array)

    # 1. Base case
    if n == 1:
        return array
    
    mid = len(array) // 2

    # 2. Recursive case
    left_half = merge_sort(array[:mid])
    right_half = merge_sort(array[mid:])

    # 3. Merge subarrays
    return merge(left_half, right_half)


def merge(left: list[int], right: list[int]) -> list[int]:
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result



numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
# print(merge_sort(numbers))


def quick_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums
    
    pivot = nums[-1]
    smaller, equal, greater = [], [], []

    for num in nums:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            greater.append(num)

    return quick_sort(smaller) + equal + quick_sort(greater)


# print(quick_sort(numbers))


# print(
#     timeit.timeit(
#         f"quick_sort({numbers})",
#         setup="""from __main__ import quick_sort""",
#         number=100000
#     )
# )

