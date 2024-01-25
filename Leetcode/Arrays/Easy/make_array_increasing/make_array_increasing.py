class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) == 2:
            return True
        for i in range(len(nums)-1, -1, -1):
            digit = nums.pop(i)
            if len(set(nums)) == len(nums) and nums == sorted(nums):
                return True
            else:
                nums.insert(i, digit)
        return False
