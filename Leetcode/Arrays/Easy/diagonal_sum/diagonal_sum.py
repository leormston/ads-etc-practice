class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        prim = 0
        sec = len(mat) - 1
        #going row by row
        for row in mat:
            total += row[prim]
            if prim != sec:
                total += row[sec]
            prim += 1
            sec -= 1
        return total