class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros = []
        
        m = len(matrix)
        n = len(matrix[0])
        
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zeros.append((row,col))
                    
        for pos in zeros:
            for vert in range(n):
                print("vert:",pos[0], vert)
                matrix[pos[0]][vert] = 0
            for horiz in range(m):
                print(horiz,pos[1])
                matrix[horiz][pos[1]] = 0
        
        print(zeros)