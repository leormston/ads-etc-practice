class Solution:
    def maxScore(self, s: str) -> int:
        s = list(s)
        ma = 0
        for i in range(1, len(s)):
            print(f"Group {i}")
            if s[0:i].count("0") + s[i:].count("1") > ma:
                ma = s[0:i].count("0") + s[i:].count("1")
        return ma