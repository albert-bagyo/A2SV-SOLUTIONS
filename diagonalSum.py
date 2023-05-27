class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        s = 0
        for i in range(l):
            s += mat[i][i] + mat[i][l - i - 1]
        if l % 2 != 0:
            mid = l  // 2
            s -= mat[mid][mid]
        return s 
