class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 1:
            return grid[0][0]
        total = 0
        while len(grid[-1]) > 0:
            max_v = 0
            for i in range(len(grid)):
                max_val = max(grid[i])
                grid[i].remove(max_val)
                max_v = max([max_v, max_val])
            print(max_v)
            total += max_v
        return total