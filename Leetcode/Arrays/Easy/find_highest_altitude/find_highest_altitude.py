class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        for altitude in gain:
            altitudes.append(altitudes[-1]+altitude)
        return max(altitudes)