class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        if ch in word:
            i = word.index(ch)
            pre = "".join(word[:i+1][::-1])
            post = "".join(word[i+1:])

            return pre+post
        else:
            return "".join(word)
            