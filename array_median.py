from typing import List
import math

def findMedianSortedArrays(nums1: List[int], nums2: List[int]):

    merged =  nums1 + nums2
    merged.sort()

    pos = (len(merged) - 1) / 2
    pos_l = math.floor(pos)
    pos_r = math.ceil(pos)

    median = (merged[pos_l] + merged[pos_r]) / 2

    return median


def main():
    arr1 = [1, 2, 3]
    arr2 = [4, 5, 6]

    median1 = findMedianSortedArrays(arr1, arr2)
    print(median1)

    arr3 = [1, 3]
    arr4 = [2]
    median2 = findMedianSortedArrays(arr3, arr4)
    print(median2)


if __name__ == "__main__":
    main()