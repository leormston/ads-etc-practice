class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", 
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        unique_words = set([])
        for word in words:
            word = list(word)
            morse_tran = ""
            for letter in word:
                morse_tran += morse[alphabet.index(letter)]
            unique_words.add(morse_tran)
        print(unique_words)
        return len(set(unique_words))