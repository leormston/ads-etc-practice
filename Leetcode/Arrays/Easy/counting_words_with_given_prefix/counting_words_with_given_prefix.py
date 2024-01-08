class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        pref = list(pref)
        length = len(pref)
        for word in words:
            word = list(word)
            if len(word) >= length and word[:length] == pref:
                count += 1
        return count