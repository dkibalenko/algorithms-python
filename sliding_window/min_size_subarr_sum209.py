def min_adjacent_sliding_window(nums: list[int], target: int) -> int:
    # set left var
    # set total sum var
    # set min_len var

    # expand window
    # run for loop with right var - bounds - full pass
    # sum up total sum with right item
    
    # shrink window
    # run while loop when total >= target
    # update min_len
    # subtract left item from total
    # move left

    left = 0
    total = 0
    min_len = float("inf")

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            min_len = min(min_len, right - left + 1)
            total -= nums[left]
            left += 1

    return min_len if min_len != float("inf") else 0


print(min_adjacent_sliding_window([2, 3, 1, 2, 4, 3], 7))
