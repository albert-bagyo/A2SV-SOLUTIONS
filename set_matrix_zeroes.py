class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def setZero(x,y):
            for i in range(rows):
                matrix[i][y] = 0
            
            for j in range(cols):
                matrix[x][j] = 0

        coords = []
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    coords.append((i,j))

        for x, y in coords:
            setZero(x,y)
