class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while nums.count(original) > 0:
            original = original * 2
        return original