import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = date1.split("-")
        date1 = [int(i) for i in date1]
        start = datetime.date(date1[0], date1[1], date1[2])
        date2 = date2.split("-")
        date1 = [int(i) for i in date1]
        date2 = [int(i) for i in date2]
        end = datetime.date(date2[0], date2[1], date2[2])

        return max((end - start).days, (start - end ).days)

