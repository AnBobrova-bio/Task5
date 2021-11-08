def medians(nums1, nums2):
    nums3 = nums1 + nums2
    nums3new = list(set(nums3))
    nums3new.sort()
    print(nums3new)
    if len(nums3new) % 2 == 1:
        print(nums3new[len(nums3new)//2])
    else:
        k = (len(nums3new) // 2)
        print((nums3new[k-1] + nums3new[k]) / 2)

nums1 = str(input())
nums2 = str(input())
medians(nums1, nums2)