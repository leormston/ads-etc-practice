class Solution:
    def minimumSum(self, num: int) -> int:
        arr = [int(x) for x in str(num)]
        arr = sorted(arr)
        num1 = ""
        num2 = ""
        flip = False
        while len(arr) > 0:
            if not flip:
                num1 += str(arr.pop(0))
                flip = True
            else:
                num2 += str(arr.pop(0))
                flip = False
        print(int(num1), int(num2))
        return int(num1) + int(num2)