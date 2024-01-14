class Solution:
    def hammingWeight(self, n: int) -> int:
        return list(str(bin(n))[2:]).count("1")