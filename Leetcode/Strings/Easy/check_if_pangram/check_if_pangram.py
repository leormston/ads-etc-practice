class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(list(sentence.lower()))) == 26