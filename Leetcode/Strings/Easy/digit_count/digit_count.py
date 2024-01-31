class Solution:
    def digitCount(self, num: str) -> bool:
        num = [int(x) for x in num]
        for i in range(len(num)):
            if num.count(i) != num[i]:
                return False
        return True