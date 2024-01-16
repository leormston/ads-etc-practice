class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        plate = list(licensePlate.lower())
        new_plate = []
        for letter in plate:
            if letter in alpha:
                new_plate.append(letter)
        shortest = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
        for word in words:
            invalid = False
            for char in new_plate:
                if new_plate.count(char) > word.count(char):
                    invalid = True
            if not invalid:
                if len(word) < len(shortest):
                    shortest = word


        return shortest