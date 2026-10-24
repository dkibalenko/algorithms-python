from collections import defaultdict, Counter


def containsDuplicate(nums):
    """Brute Force, Time O(n^2), Space O(1)."""
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


def containsDuplicate2(nums):
    """Use .sort(), Time O(n log n), Space O(1)."""

    nums.sort()  # first sort items

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:  # if any adjacent items are the same
            return True
    return False


def containsDuplicate3(nums):
    """Use set() to eliminate duplicates, Time O(n), Space O(k)."""

    seen = set()

    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def containsDuplicate4(nums):
    """Use set(), Time O(n), Space O(k)."""
    return len(set(nums)) < len(nums)


def containsDuplicate5(nums):
    """Use dict for storing items and their counts. Time O(n), Space O(k)."""

    seen = {}

    for num in nums:
        if num in seen:
            return True
        seen[num] = 1

    # for num in nums:
    #     if num in seen and seen[num] >= 1: 
    #         return True
    #     seen[num] = seen.get(num, 0) + 1


def containsDuplicate6(nums):
    """Use defaultldict from collections, Time O(n + n), Space O(k)."""
  
    # counts = defaultdict(lambda: 1)  # 1 by default. O(n) build
    counts = defaultdict(int)  # defalut 0
  
    for item in nums:
        # if counts[item] > 1:
        if counts[item] >= 1:
            return True

        counts[item] += 1
  
    return False


def containsDuplicate7(nums):
    """Use Counter class from collections, Time O(n + n), Space O(k)."""

    counted = Counter(nums)  # O(n) build

    for item in counted.values():  # O(n)
        if item > 1:
            return True

    return False


print(containsDuplicate6([1, 2, 3, 4]))
