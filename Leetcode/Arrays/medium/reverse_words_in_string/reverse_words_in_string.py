class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = []
        words = list(s)
        word = ""
        for i in range(len(words)):
            if words[i] == " ":
                if len(word) > 0:
                    word_list.append(word)
                    word = ""
            else:
                word += words[i]
                if i == len(words) -1:
                    word_list.append(word)
        final_str = ""
        for index in range(len(word_list)-1, -1, -1):
            final_str += word_list[index]
            if index != 0:
                final_str += " "
        return final_str

