class Solution:
    def findGCD(self, nums: List[int]) -> int:
        lowest = min(nums)
        highest = max(nums)
        for i in range(lowest, 0, -1):
            if lowest % i == 0 and highest % i == 0:
                return i
        return -1