import math
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {}
        for i in nums:
            if str(i) not in counts:
                counts[str(i)] = 1
            else:
                count = counts[str(i)]
                count += 1
                if count > math.ceil(len(nums) / 2):
                    return i
                else:
                    counts[str(i)] = count
        return nums[0]
