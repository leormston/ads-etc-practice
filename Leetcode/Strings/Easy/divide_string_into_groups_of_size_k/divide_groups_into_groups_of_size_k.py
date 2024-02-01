class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s = list(s)
        arr = []
        while len(s) > k - 1:
            x = "".join(s[0:k])
            arr.append(x)
            count = 0
            while count < k :
                s.pop(0)
                count +=1
        if len(s) > 0:
            fill = fill * (k - len(s))
            arr.append("".join(s) + fill)

        return arr
