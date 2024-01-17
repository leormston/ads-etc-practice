class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = []
        for i in nums:
            if i in seen:
                return i
            else:
                seen.append(i)