class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if len(nums) == 2 or len(nums) == 1:
            return -1
        return nums[1]