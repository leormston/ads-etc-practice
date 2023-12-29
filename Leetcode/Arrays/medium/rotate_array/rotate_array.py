class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = k
        if k > len(nums):
            r = len(nums) - k
        if r < 0:
            r = int(r / -1)
        if r > len(nums):
            r = r % len(nums) 
        arr = []
        arr = nums[len(nums) - r::]
        for i in range(len(arr)-1, -1, -1):
            nums.pop(-1)
            nums.insert(0, arr[i])
