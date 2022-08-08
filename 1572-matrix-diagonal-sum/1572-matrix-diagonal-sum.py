class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        rows = len(mat)
        col = len(mat[0])
        s=0
        for i in range(rows):
            s+=mat[i][i]
        for j in range(col):
            if [j]!=[(col-1)-j]:
                s+=mat[j][(col-1)-j]
        return s
        