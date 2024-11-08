def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    result = list(set1 & set2)

    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))