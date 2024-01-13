class Solution:
    def isPalindrome(self, s: str) -> bool:
        alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        s = "".join(s.split()).lower()
        word = ""
        for char in s:
            if char in alp:
                word += char
        length = len(word)
        if length == 0:
            return True
        if length == 1:
            return True
        if length % 2 == 0:
            return word[:int(length/2)] == word[int(length/2):][::-1]
        return word[:int(length/2)] == word[int(length/2)+1:][::-1]