class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        s = list(s)
        exc = ["C", "L", "X", "V", "I"]
        while(len(s) > 0):
            char = s[0]
            if char == "D":
                total += 500
            elif char == "M":
                total += 1000
            elif char == "L":
                total += 50
            elif char == "V":
                total += 5
            elif char == "I":
                if len(s) > 1 and s[1] != "I":
                    if s[1] == "V":
                        total += 4
                    elif s[1] == "X":
                        total += 9
                    s.pop(0)
                else:
                    total += 1
            elif char == "X":
                if len(s) > 1 and s[1] not in exc[2:]:
                    if s[1] == "L":
                        total += 40
                    elif s[1] == "C":
                        total += 90
                    s.pop(0)
                else:
                    total += 10
            elif char == "C":
                if len(s) > 1 and s[1] not in exc:
                    if s[1] == "D":
                        total += 400
                    elif s[1] == "M":
                        total += 900
                    s.pop(0)
                else:
                    total += 100
            s.pop(0)
        return total