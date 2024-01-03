class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        total = 0
        i = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                for z in range(j, len(nums)):
                    if nums[j] - nums[i] == diff and nums[z] - nums[j] == diff:
                        total += 1
        return total