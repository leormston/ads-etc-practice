class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = []
        for i in range(0, len(nums), 2):
            even.append(nums[i])
        odd = []
        for i in range(1, len(nums), 2):
            odd.append(nums[i])
        
        even = sorted(even)
        odd = sorted(odd)[::-1]

        new = []
        for i in range(len(nums)):
            if i % 2 == 0:
                new.append(even.pop(0))
            else:
                new.append(odd.pop(0))
        

        return new