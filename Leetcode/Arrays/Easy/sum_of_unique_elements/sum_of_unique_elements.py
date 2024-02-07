class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        se = list(set(nums))
        unique = []
        for i in se:
            if nums.count(i) == 1:
                unique.append(i)
        return sum(unique)