class Solution:
    def isHappy(self, n: int) -> bool:
        ans = n
        seen = []
        while True:
            ans = sum([int(i) * int(i) for i in str(ans)])
            if ans == 1:
                return True
            elif ans in seen:
                return False
            else:
                seen.append(ans)
        return False