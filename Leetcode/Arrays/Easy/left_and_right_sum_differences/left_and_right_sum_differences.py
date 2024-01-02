class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        left_sums = []
        right_sums = []
        for index in range(len(nums)):
            if index == 0:
                ans = 0 -sum(nums[index+1:])
                answer.append(max(ans, -ans))
            else:
                ans = sum(nums[0:index]) - sum(nums[index+1:])
                answer.append(max(ans, -ans))

        return answer
