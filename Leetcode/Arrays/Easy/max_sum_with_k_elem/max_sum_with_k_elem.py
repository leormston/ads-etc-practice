class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        num = max(nums)
        nums = []
        for i in range(k):
            nums.append(num)
            num+=1
        return sum(nums)