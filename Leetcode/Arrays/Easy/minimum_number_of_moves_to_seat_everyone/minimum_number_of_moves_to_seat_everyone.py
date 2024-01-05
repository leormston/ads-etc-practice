class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        total = 0
        for i in range(len(students)):
            total += max((students[i]-seats[i]), -(students[i]-seats[i]))

        return total