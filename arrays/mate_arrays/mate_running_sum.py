from itertools import accumulate


def running_sum(nums):
    sums_list = [nums[0]]

    for i in range(1, len(nums)):
        sums_list.append(sums_list[i-1] + nums[i])

    return sums_list


def running_sum2(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


def running_sum3(nums):
    return list(accumulate(nums))


array = [3, 1, 2, 10, 1]

print(running_sum3(array))


def test(nums):
    result = [nums[0]]

    for i in range(1, len(nums)):
        result.append(result[i - 1] + nums[i])
    
    result

