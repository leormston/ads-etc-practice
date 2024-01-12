class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ["a", "e", "i", "o", "u"]
        half_one = s[:int(len(s) / 2)]
        half_two = s[int(len(s) / 2):]
        count_one = 0
        count_two = 0

        for letter in half_one:
            if letter.lower() in vowels:
                count_one += 1
        for letter in half_two:
            if letter.lower() in vowels:
                count_two += 1
        return count_one == count_two