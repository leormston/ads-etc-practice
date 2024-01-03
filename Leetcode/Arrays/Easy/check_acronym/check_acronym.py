class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        string = ""
        for word in words:
            word = list(word)
            string += word[0]
        return string == s
            