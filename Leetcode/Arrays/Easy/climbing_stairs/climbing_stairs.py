class Solution:
    #old method no good as exponential growth
    # def walk(self, count):
    #     if count < 0:
    #         return 0
    #     if count == 0 or count == 1:
    #         return 1
    #     return self.walk(count-1) + self.walk(count - 2)

    #using fibonacci sequence instead
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        else:
            arr = [1, 1]
            total = arr[-1]
            for i in range(1,n):
                arr.append(arr[-1] + arr[-2])
            return arr[-1]
