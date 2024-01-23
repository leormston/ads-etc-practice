class Solution:
    def makeFancyString(self, s: str) -> str:
        seq = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj", "kkk", "lll", "mmm", "nnn", "ooo", "ppp", "qqq", "rrr", "sss", "ttt", "uuu", "vvv", "www", "xxx", "yyy", "zzz"]
        for r in seq:
            while s.count(r) > 0:
                s = s.replace(r, r[:-1])
        return s