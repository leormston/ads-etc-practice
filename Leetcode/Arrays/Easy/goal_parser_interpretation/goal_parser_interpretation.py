class Solution:
    def interpret(self, command: str) -> str:
        string = ""
        current_string = ""
        for letter in command:
            current_string += letter
            if current_string == "G":
                string += "G"
                current_string = ""
            elif current_string == "()":
                string += "o"
                current_string = ""
            elif current_string == "(al)":
                string += "al"
                current_string = ""

        return string