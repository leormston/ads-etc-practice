import sys
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        sys.set_int_max_str_digits(100000)
        return [int(i) for i in list(str(int("".join([str(i) for i in num])) + k))]