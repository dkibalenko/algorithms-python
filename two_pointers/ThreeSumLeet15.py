def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []

    for i in range(len(nums) - 2):
        # Skip duplicate fixed values
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # move both inward
                left += 1
                right -= 1

                # duplicate would be behind you
                # Skip duplicates for left pointer
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicates for right pointer
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < 0:
                left += 1
            else:
                right -= 1

    return result


three_sum([-1, 0, 1 , 2, -1, -4])
