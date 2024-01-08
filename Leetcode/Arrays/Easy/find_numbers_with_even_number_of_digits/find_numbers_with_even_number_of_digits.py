class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        len_arr = [len(str(num)) for num in nums]
        for length in len_arr:
            if int(length) % 2 == 0:
                count += 1
        return count