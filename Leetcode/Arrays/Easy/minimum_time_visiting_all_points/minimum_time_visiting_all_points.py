class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time = 0
        start = points[0]
        for i in range(1, len(points)):
            time += max([max(start[0] - points[i][0], -(start[0] - points[i][0])), max(start[1] - points[i][1], -(start[1] - points[i][1]))])
            start = points[i]
        return time