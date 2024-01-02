class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        total = 0
        while len(nums)  >=2:
            num = nums.pop(0)
            for i in nums:
                if num + i < target:
                    total +=1
        return total