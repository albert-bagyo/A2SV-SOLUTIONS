class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = []
        rows = len(mat)
        cols = len(mat[0])

        if rows * cols != r * c:
            return mat
        
        x = y = 1
        for i in range(r):
            row = []
            for j in range(c):
                row.append(mat[x - 1][y - 1])#access the matrix in sequncial manner
                x += y // (cols)
                y = (y % cols) + 1
            res.append(row)
        
        return res
