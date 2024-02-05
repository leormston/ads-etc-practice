class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        se = set(s)
        pos = float('inf')
        ind = -1
        for i in se:
            if s.count(i) == 1 and s.index(i)  < pos:
                pos = s.index(i)
                ind = s.index(i)
        return ind