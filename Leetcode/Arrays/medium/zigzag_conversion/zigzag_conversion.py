class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row_dict = {}
        row = 0
        direction = "down"
        if numRows == 1:
            return s
        for i in s:
            if row == numRows -1:
                direction = "up"
            if row == 0:
                direction = "down"
            if str(row) in row_dict:
                string = row_dict[str(row)]
                row_dict[str(row)] = string + i
            else:
                row_dict[str(row)] = i
            if direction == "down":
                row += 1
            if direction == "up":
                row -= 1
        final_str = ""
        for row in range(numRows):
            if str(row) in row_dict:
                final_str += row_dict[str(row)]
        return final_str