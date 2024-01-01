class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)[::-1]
        count = 0
        for i in citations:
            if i > count:
                count += 1
        return count
