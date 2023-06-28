class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row_count = len(matrix)
        col_count = len(matrix[0])

        for r in range(row_count):
            first = matrix[r][0]
            for row, col in zip(range(r,row_count), range(col_count)):
                if matrix[row][col] != first:
                    return False

        if col_count == 1:
            return True

        for c in range(1,col_count):
            first = matrix[0][c]
            for row, col in zip(range(row_count), range(c, col_count)):
                if matrix[row][col] != first:
                    return False

        return True
