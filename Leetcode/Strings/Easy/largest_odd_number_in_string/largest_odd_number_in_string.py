import sys

sys.set_int_max_str_digits(100000)
class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd = ["1", "3", "5", "7", "9"]
        if len(num) == 0:
            return ""
        count = len(num) - 1
        while count >= 0:
            if num[count] in odd:
                return num[:count+1]
            count -= 1
        return ""