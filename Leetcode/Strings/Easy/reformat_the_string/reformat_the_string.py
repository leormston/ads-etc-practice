class Solution:
    def reformat(self, s: str) -> str:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

        s = [x for x in list(s)]
        let = []
        num = []
        for i in s:
            if i in alpha:
                let.append(i)
            else:
                num.append(i)
        diff = len(let) - len(num)
        if max(diff, -diff) > 1:
            return ""
        string = ""
        if len(let) == len(num) - 1:
            while len(num) > 0:
                string += num.pop(0)
                if len(let) > 0:
                    string += let.pop(0)
        elif len(let) == len(num):
            while(len(num) > 0):
                string += let.pop(0)
                string += num.pop(0)
        elif len(let) == len(num) + 1:
            while len(let) > 0:
                string += let.pop(0)
                if len(num) > 0:
                    string += num.pop(0)
        return string
        