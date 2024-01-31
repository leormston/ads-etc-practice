class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        target = [x for x in target]
        s = [x for x in s]
        index = 0
        count = 0
        while s.count(target[index]) > 0:
            s.pop(s.index(target[index]))
            if index == len(target) - 1:
                count += 1
                index = 0
            else:
                index += 1
        return count
