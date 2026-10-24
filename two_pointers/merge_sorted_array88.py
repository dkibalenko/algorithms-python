def merge(nums1, m, nums2, n):
    x, y = m - 1, n - 1

    for z in range(m + n - 1, -1, -1):
        # stop logic - pointers out of bounds
        if y < 0:
            break
        if x < 0:
            nums1[z] = nums2[y]
            y -= 1
            continue

        # comparison logic - happy path
        if nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1

    return nums1


print(merge([4, 7, 8, 9, 0, 0, 0], 4, [2, 5, 6], 3))
