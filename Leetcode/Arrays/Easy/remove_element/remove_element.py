class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index, count = 0, 0
        while(index != len(nums)):
            if nums[index] == val: nums.pop(index)
            else: index, count = index + 1, count + 1
        return count 
                