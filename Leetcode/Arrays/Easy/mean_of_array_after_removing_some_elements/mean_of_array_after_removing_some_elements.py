class Solution:
    def trimMean(self, arr: List[int]) -> float:
        cuts = int(len(arr) * 0.05)
        arr = sorted(arr)[cuts:-cuts]
        return sum(arr) / len(arr)