class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        s = list(s)
        a = list(set(s))
        count = s.count(s[0])
        for i in a:
            if s.count(i) != count:
                return False
        return True