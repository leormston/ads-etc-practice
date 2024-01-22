class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = list(brokenLetters)
        count = 0
        words = text.split()

        for word in words:
            typable = True
            for char in list(word):
                if char in broken:
                    typable = False
            if typable:
                count += 1

        return count