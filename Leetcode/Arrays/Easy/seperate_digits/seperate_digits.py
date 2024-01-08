class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        string = ""
        for num in nums:
            string += str(num)
        print(string)
        return [int(char) for char in list(string)]