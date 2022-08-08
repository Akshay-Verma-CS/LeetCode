class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        var = len(matrix[0])
        resMatrix = [[] for i in range(var)]
        for i in range(n):
            for j in range(var):
                resMatrix[j].append(matrix[i][j])
        return resMatrix
            
            