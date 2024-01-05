class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        output = []
        while len(heights)> 0:
            height = max(heights)
            height_index = heights.index(height)
            output.append(names[height_index])
            names.pop(height_index)
            heights.pop(height_index)
        return output