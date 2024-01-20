class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        seen = []
        for i in key:
            if i == ' ':
                continue
            if i not in seen:
                seen.append(i)
        new_string = ''
        for i in message:
            if i == ' ':
                new_string += i
            else:
                new_string += alpha[seen.index(i)]

        return new_string