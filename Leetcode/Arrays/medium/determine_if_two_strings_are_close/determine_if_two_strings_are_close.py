class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        let1 = set(list(word1))
        let2 = set(list(word2))
        if let1 != let2:
            return False
        for char in let1:
            if char not in let2:
                return False
        word1counts = {}
        word2counts = {}
        for char in let1:
            word1count = str(list(word1).count(char))
            word2count = str(list(word2).count(char))

            if word1count in word1counts:
                temp = word1counts[word1count]
                temp.append(char)
                word1counts[word1count] = temp
            else:
                word1counts[word1count] = [char]
            if word2count in word2counts:
                temp = word2counts[word2count]
                temp.append(char)
                word2counts[word2count] = temp
            else:
                word2counts[word2count] = [char]
        for key in word1counts:
            if key not in word2counts:
                return False
            if len(word1counts[key]) != len(word2counts[key]):
                return False


        # #see if similar count for another word
        # for char in list(word1):
        #     if list(word1).count(char) != list(word2).count(char):
        #         return False
        return True