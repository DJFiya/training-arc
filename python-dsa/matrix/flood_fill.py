"""
Flood fill algorithm. Not too difficult, but decided to do the non-recursive version.
"""

class FloodFill():
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        rmax, cmax = len(image), len(image[0])
        base_clr = image[sr][sc]
        fillings = [(sr, sc)]
        while fillings:
            row, col = fillings.pop()
            if row < 0 or row >= rmax or col < 0 or col >= cmax or image[row][col] == color or (not image[row][col] == base_clr):
                continue
            image[row][col] = color
            for point in ((row-1, col), (row+1, col), (row, col-1), (row, col+1)):
                fillings.append(point)
        return image