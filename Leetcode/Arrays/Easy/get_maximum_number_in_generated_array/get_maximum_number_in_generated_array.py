class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 1 or n == 0:
            return n
        arr = [0] * (n+1)
        for i in range(n):
            if i == 0 or i == 1:
                arr[i] = i
            if 2 <= 2 * i <= n:
                arr[2 * i] = arr[i]
            if 2<= 2 * i + 1 <= n:
                arr[2 * i + 1] = arr[i] + arr[i + 1]
        
        return max(arr)