class Solution:
    def checkFromPoint(self, sequence, word, ma, index):
        count = 0
        while index <= len(sequence):
            if sequence[index:index+len(word)] == word:
                
                count += 1
                if count > ma:
                    ma = count
                index += len(word)
            else:
                count = 0
                index += 1
        return ma
    def maxRepeating(self, sequence: str, word: str) -> int:
        if sequence.count(word) == 0:
            return 0
        
        if sequence.count(word) == 1:
            return 1

        else:
            ma = 0
            for i in range(len(sequence)-len(word)):
                ma = self.checkFromPoint(sequence, word, ma, i)
        return ma

