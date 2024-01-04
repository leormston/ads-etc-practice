class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        unique = []
        counts = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                # print(nums[i:j])
                unique.append(nums[i:j])
                count = set(nums[i:j])
                counts.append(len(count))
        total = 0
        for count in counts:
            total += count * count
        return total