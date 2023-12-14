class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        count = 0
        while(index != len(nums)):
            print(nums)
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
                count += 1
        return count
                