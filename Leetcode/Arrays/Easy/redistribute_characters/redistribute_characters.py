class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        for word in words:
            for letter in word:
                if letter in dic:
                    count = dic[letter]
                    dic[letter] = count + 1
                else:
                    dic[letter] = 1
        for k,v in dic.items():
            if v % len(words) != 0:
                return False
        return True