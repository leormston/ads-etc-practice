class Solution:
    def freqAlphabets(self, s: str) -> str:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        s = list(s)
        print(s[2])
        string = ""
        while len(s) > 0:
            if len(s) == 1 or len(s) == 2:
                char = int(s.pop(0))
                string += alpha[char-1]
            else:
                if s[2] == '#':
                    char = int(s[0] + s[1])
                    string += alpha[char-1]
                    s.pop(0)
                    s.pop(0)
                    s.pop(0)
                else:
                    char = int(s.pop(0))
                    string += alpha[char-1]

        return string


