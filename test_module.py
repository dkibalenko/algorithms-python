import pytest


def max_subarr3(nums: list[int]) -> int:
    max_sum = nums[0]
    current_sum = 0

    for i in range(len(nums)):
        if current_sum < 0:
            current_sum = 0

        current_sum += nums[i]
        max_sum = max(current_sum, max_sum)

    return max_sum


@pytest.mark.parametrize("nums, expected", [
    pytest.param([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, id="general_case"),
    pytest.param([5], 5, id="single_element"),
    pytest.param([-3, -1, -2], -1, id="extreme_all_negative"),
    pytest.param([5, 4, -1, 7, 8], 23, id="extra_case"),
])
def test_max_subarr3_general_and_extreme(nums, expected):
    assert max_subarr3(nums) == expected

# =================================================

# def movezeros(nums):
#     slow = 0
#     fast = 0

#     while fast < len(nums):
#         if nums[fast]:
#             nums[slow], nums[fast] = nums[fast], nums[slow]
#             slow += 1

#         fast += 1
#     return nums


# @pytest.mark.parametrize("nums, expected", [
#     pytest.param([0, 1, 0, 3, 12], [1, 3, 12, 0, 0], id="general_case"),
#     pytest.param([1, 0, -2, 4, 0, -5, 9], [1, -2, 4, -5, 9, 0, 0], id="negatives_present"),
#     pytest.param([2, 2, 2, 2], [2, 2, 2, 2], id="extreme_all_duplicates"),
#     pytest.param([0], [0], id="extreme_one_item"),
#     pytest.param([], [], id="extreme_empty_nums"),
# ])
# def test_movezeros(nums, expected):
#     assert movezeros(nums) == expected


# ============================================


# def merge(nums1, m, nums2, n):
#     x, y = m - 1, n - 1

#     for i in range(len(nums1) - 1, -1, -1):
#         # stop logic - pointer out of bounds
#         if x < 0:
#             nums1[i] = nums2[y]
#             y -= 1
#             continue
#         if y < 0:
#             break

#         # comparison logic - happy path
#         if nums1[x] > nums2[y]:
#             nums1[i] = nums1[x]
#             x -= 1
#         else:
#             nums1[i] = nums2[y]
#             y -= 1

#     return nums1


# import pytest


# @pytest.mark.parametrize(
#     "nums1, m, nums2, n, expected",
#     [
#         pytest.param([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6], id="general_case"),
#         pytest.param([1], 1, [], 0, [1], id="extreme_nums2_empty"),
#         pytest.param([0], 0, [1], 1, [1], id="extreme_nums1_all_placeholder"),
#         pytest.param([2, 2, 3, 0, 0], 3, [2, 5], 2, [2, 2, 2, 3, 5], id="extreme_duplicates_across_both"),
#     ]
# )
# def test_merge_general_and_extreme(nums1, m, nums2, n, expected):
#     assert merge(nums1, m, nums2, n) == expected
