class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        password = list(password)
        if len(password) < 8:
            return False
        
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        alpha_upper = [x.upper() for x in alpha]
        caps = False
        lower = False
        dig = False
        spec = False
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        special = [x for x in "!@#$%^&*()-+"]
        last = None
        for letter in password:
            if letter == last:
                return False
            elif letter in alpha:
                lower = True
            elif letter in alpha_upper:
                caps = True
            elif letter in digits:
                dig = True
            elif letter in special:
                spec = True
            last = letter

        return caps and lower and dig and spec
