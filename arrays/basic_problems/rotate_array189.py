def reverse_items(left: int, right: int, arr: list):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate(nums, k):
    k = k % len(nums)

    reverse_items(0, len(nums) - 1, nums)
    reverse_items(0, k - 1, nums)
    reverse_items(k, len(nums) - 1, nums)

    return nums


print(rotate([1, 2, 3, 4, 5, 6, 7], 3))
