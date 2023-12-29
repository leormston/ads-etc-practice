#old solution (recursive but too slow / complex):
class Solution:
    def jump(self, nums, jump_amount, index, visited):
        if index == len(nums) - 1:
            return True
        if jump_amount == 0:
            return False
        if index in visited:
            return False
        new_index = jump_amount + index
        if new_index > len(nums) - 1:
            return False
        for i in range(0, nums[new_index]+1):
            if self.jump(nums, i, new_index, visited) == True:
                return True
        visited.append(new_index)
        return False

    def canJump(self, nums: List[int]) -> bool:
        end = False
        start = nums[0]
        dead_ends = []
        for i in range(start+1):
            if self.jump(nums, i, 0, dead_ends) == True:
                return True
        return False

        
#new solution (much simpler and quicker)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        for i in range(len(nums)-2, -1, -1):
            #this works as if it is greater that means we can reach it
            if i + nums[i] >= target:
                target = i
        if target == 0:
            return True
        else:
            return False