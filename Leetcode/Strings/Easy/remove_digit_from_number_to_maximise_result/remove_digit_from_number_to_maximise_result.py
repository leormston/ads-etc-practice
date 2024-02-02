class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ma = 0
        index = 0
        number = list(str(number))
        while index < len(number):
            if number[index] == digit:
                number.pop(index)
                if int("".join(number)) > ma:
                    print( int("".join(number)))
                    ma = int("".join(number))
                number.insert(index, digit )
            index += 1
        return str(ma)