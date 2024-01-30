class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        arr = []
        js = []
        for i in range(len(nums)):
            if nums[i] == key:
                js.append(i)
        js = list(set(js))
        for i in range(len(nums)):
            for j in js:
                if max((i-j), -(i-j)) <= k:
                    arr.append(i)
        return set(arr)