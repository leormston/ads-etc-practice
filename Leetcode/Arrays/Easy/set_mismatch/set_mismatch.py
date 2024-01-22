class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        uni = list(set(nums))
        counts = [i for i in range(1, len(nums)+1)]
        multi = None
        missing = None
        for num in counts:
            if multi is not None and missing is not None:
                return [multi, missing]
            if nums.count(num) > 1:
                multi = num
            if num not in nums:
                missing = num
        return [multi, missing]