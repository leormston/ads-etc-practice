class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        totals = [sum(arr)]
        sizes = []
        for i in range(len(arr)+1):
            if i % 2 != 0:
                sizes.append(i)
        sizes.pop(0)
        print(sizes)
        for i in range(len(arr)):
            for s in sizes:
                if i + s <= len(arr):
                    totals.append(sum(arr[i: i+s]))
        return sum(totals)