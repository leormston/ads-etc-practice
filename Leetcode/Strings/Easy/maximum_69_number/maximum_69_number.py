class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        if num.count("6") == 0:
            return int("".join(num))
        else:
            index = num.index("6")
            num[index] = "9"
        return int("".join(num))