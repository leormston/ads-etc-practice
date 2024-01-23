class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        search = ["b", "a", "l", "l", "o", "o", "n"]

        ptr = 0
        count = 0
        text = list(text)
        while text.count(search[ptr]) > 0:
            index = text.index(search[ptr])
            text.pop(index)
            if ptr == 6:
                ptr = 0
                count +=1
            else:
                ptr += 1
        return count