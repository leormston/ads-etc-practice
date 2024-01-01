class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for i in nums:
            total = total * i
        arr = []
        for i in range(len(nums)):
            if nums[i] == 0:
                temp_t = 1
                for j in range(len(nums)):
                    if j == i:
                        temp_t = temp_t
                    else:
                        temp_t = temp_t * nums[j]
                arr.append(int(temp_t))
            else:
                arr.append(int(total / nums[i]))
        return arr