class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u"]
        s = list(s)
        v = []
        indexes = []
        for i in range(len(s)):
            if s[i].lower() in vowels:
                v.append(s[i])
                indexes.append(i)
        indexes = indexes[::-1]
        for i in range(len(v)):
            s[indexes[i]] = v[i]
        return "".join(s)
            