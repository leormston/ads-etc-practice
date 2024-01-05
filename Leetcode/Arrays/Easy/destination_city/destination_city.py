from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts = []
        ends =  []
        for i in paths:
            starts.append(i[0])
            ends.append(i[1])
        for e in ends:
            if e not in starts:
                return e