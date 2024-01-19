class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        dp = [[0] * c for _ in range(r)]

        for j in range(c):
            dp[0][j] = matrix[0][j]
        
        for i in range(1, r):
            for j in range(c):
                ld = rd = float('inf')
                up = matrix[i][j] + dp[i-1][j]

                if j - 1 >= 0:
                    ld = matrix[i][j] + dp[i-1][j-1]
                if j + 1 < c:
                    rd = matrix[i][j] + dp[i - 1][j+1]
                
                dp[i][j] = min(up, min(ld, rd))
        mini = dp[r - 1][0]

        for j in range(1, c):
            mini = min(mini, dp[r-1][j])
        return mini