class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ignore = ["!", "?", "'", ",", ";", ".", '"']
        paragraph = " ".join(paragraph.split(",")).split()
        new_p = []
        for word in paragraph:
            word = list(word)
            for char in word:
                if char in ignore:
                    word.remove(char)
            new_p.append("".join(word).lower())
        dic = {}
        for word in new_p:
            print(word)
            if word not in banned:
                if word not in dic:
                    dic[word] = 1
                else:
                    count = dic[word] + 1
                    dic[word] = count
        common = 0
        common_k = ""
        for k, v in dic.items():
            if v > common:
                common = v
                common_k = k
        return common_k
