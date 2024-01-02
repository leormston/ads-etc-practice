class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(len(words)):
            word = list(words[i])
            if x in word:
                arr.append(i)
        return arr