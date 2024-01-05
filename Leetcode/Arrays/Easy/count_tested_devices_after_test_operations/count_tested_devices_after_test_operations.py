class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        count = 0
        bp = batteryPercentages
        for i in range(len(bp)):
            if bp[i] > 0:
                count += 1
                for j in range(i + 1, len(bp)):
                    bp[j] = max(0, bp[j]-1)
        return count