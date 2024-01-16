class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        target = alpha.index(target)
        for letter in letters:
            if alpha.index(letter) > target:
                return letter
        return letters[0]