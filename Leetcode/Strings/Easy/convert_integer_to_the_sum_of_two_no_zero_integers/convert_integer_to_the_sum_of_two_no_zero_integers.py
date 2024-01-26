class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        factors = []

        for i in range(n):
            for j in range(n):
                if i + j == n:
                    if str(i).count("0") == 0 and str(j).count("0") == 0:
                        return [i, j]