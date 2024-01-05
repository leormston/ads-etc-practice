class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        new_image = []
        for i in range(len(image)):
            mod_row = []
            row = image[i][::-1]
            for pixel in row:
                if pixel == 1:
                    mod_row.append(0)
                else:
                    mod_row.append(1)
            new_image.append(mod_row)

        return new_image
