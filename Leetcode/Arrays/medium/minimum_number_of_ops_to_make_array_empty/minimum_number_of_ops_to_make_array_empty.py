class Solution:
    def calc_ops(self, count: int) -> int:
        if count == 2: 
            return 1
        #n can be divisible by three (3, 6, 9) fastest way
        elif count % 3 == 0:
            return count / 3
        #n-2 can be divisble by three (5, 11, 20) second fastest
        elif count % 3 == 1:
            return ((count - 4) / 3) + 2
        #n-4 can be divisible by three () third fastest way
        elif count % 3 == 2:
            return ((count - 2) / 3) + 1

    def minOperations(self, nums: List[int]) -> int:
        s_nums = sorted(nums)
        total_ops = 0
        count = 0
        current = s_nums[0]
        i = 0
        while i < len(s_nums):
            if s_nums[i] == current:
                count += 1
            else:
                if count == 1:
                    return -1
                total_ops += self.calc_ops(count)
                count = 1
                current = s_nums[i]
            i += 1
        if count == 1:
            return -1
        if count > 1:
            total_ops += self.calc_ops(count)
        
        #otherwise we return -1 since we cannot get to 0
        return int(total_ops)