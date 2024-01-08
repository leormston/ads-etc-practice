class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr = [[],[]]
        for num in nums1:
            if num not in nums2 and num not in arr[0]:
                arr[0].append(num)


        for num in nums2:
            if num not in nums1 and num not in arr[1]:
                arr[1].append(num)
        return arr