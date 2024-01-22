class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        s = list(s)
        new = s
        goal = list(goal)
        for i in range(len(goal)):
            if new == goal:
                return True
            else:
                end = new.pop(0)
                new.append(end)
        return False