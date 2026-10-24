def shuffle(nums: list[int], n: int) -> list[int]:
    """
    Build a new list by alternating elements from the first half
    and the second half of nums.
    """
    result: list[int] = []
    
    for i in range(n):  # generate indices
        result.append(nums[i])      # take from first half
        result.append(nums[i + n])  # take from second half
    return result

# Example
nums = [1, 2, 3, 4, 4, 3, 2, 1]
# print(shuffle(nums, 4))  # [1, 4, 2, 3, 3, 2, 4, 1]
