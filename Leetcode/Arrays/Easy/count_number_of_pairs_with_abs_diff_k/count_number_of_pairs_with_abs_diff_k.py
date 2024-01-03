class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                val_one = nums[i]
                val_two = nums[j]
                x = max(val_one-val_two, -(val_one-val_two))
                if x ==k:
                    total += 1
        return total
                