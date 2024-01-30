class Solution:
    def largestInteger(self, num: int) -> int:
        ptrs = []
        odd = []
        even = []
        num = [int(x) for x in list(str(num))]
        for i in range(len(num)):
            if num[i] % 2 == 0:
                ptrs.append(True)
                even.append(num[i])
            else:
                ptrs.append(False)
                odd.append(num[i])
        odd = sorted(odd)[::-1]
        even = sorted(even)[::-1]
        result = []
        for i in range(len(num)):
            if ptrs[i]:
                result.append(str(even.pop(0)))
            else:
                result.append(str(odd.pop(0)))
        return int("".join(result))
        
