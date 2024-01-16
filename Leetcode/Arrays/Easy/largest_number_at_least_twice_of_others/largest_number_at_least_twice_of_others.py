class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        for num in nums:
            if num == largest:
                continue
            else:
                if num * 2 > largest:
                    return -1
        return nums.index(largest)