class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        index = 0
        while index < len(nums):
            key = str(nums[index])
            if key in dic and dic[key] < 2:
                dic[key] += 1
                index +=1
            elif key not in dic:
                dic[key] = 1
                index +=1
            else: 
                nums.pop(index)
        return index

                