class Solution:
    def findLucky(self, arr: List[int]) -> int:
        unique = list(set(arr))[::-1]
        for num in unique:
            if arr.count(num) == num:
                return num
        return -1
        