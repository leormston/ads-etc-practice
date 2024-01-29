class Solution:
    def countEven(self, num: int) -> int:
        count =0
        for i in range(1, num+1):
            if sum([int(x) for x in list(str(i)) ]) % 2 == 0:
                print(i)
                count += 1
        return count