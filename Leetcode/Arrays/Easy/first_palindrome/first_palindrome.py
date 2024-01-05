class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            word = list(word)
            mid = int(len(word) / 2)
            print(word)
            print(word[0:mid])
            print(word[mid:][::-1])
            if len(word) % 2 == 0:

                if word[0:mid] == word[mid:][::-1]:
                    return "".join(word)
            else:
                if word[0:mid] == word[mid+1:][::-1]:
                    return "".join(word)
        return ""