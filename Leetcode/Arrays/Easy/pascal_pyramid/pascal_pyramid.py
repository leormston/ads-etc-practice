class Solution:
    def make_row(self, arr, level, target_level):
        if level == target_level:
            return arr
        else:
            level += 1
            new_arr = []
            new_arr.append(arr[0])
            for i in range(1, len(arr)):
                new_arr.append(arr[i-1] + arr[i])
            new_arr.append(arr[0])
            return self.make_row(new_arr, level, target_level)

    def getRow(self, rowIndex: int) -> List[int]:
        return self.make_row([1], 0, rowIndex)