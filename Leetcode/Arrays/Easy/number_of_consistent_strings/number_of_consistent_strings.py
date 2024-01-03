class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = list(allowed)
        count = 0
        for word in words:
            word = list(word)
            allow = True
            for char in word:
                if char not in allowed:
                    allow = False
                    break
            if allow:
                count +=1
        return count