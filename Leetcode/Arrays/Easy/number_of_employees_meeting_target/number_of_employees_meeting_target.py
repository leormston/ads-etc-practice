class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours = sorted(hours)
        while (len(hours) > 0 and hours[0] < target):
            hours.pop(0)
        return len(hours)