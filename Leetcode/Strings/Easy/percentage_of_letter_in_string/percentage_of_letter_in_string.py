import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return math.floor((100 / len(s)) * list(s).count(letter))