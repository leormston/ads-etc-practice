class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        common = nums[0]
        if len(nums) == 0:
            return common
        else:
            for i in range(len(nums)):
                if common == []:
                    return []
                count = 0 
                while(count < len(common)):
                    if common[count] not in  nums[i]:
                        common.pop(count)
                    else:
                        count += 1
        return sorted(common)
