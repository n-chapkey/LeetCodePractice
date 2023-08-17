class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix[0])

        counter = 0
        stack = []
        
        #n-i-1
        for i in range(n):
            stack.extend(matrix[i])
            matrix[i] = []
            
        print ("stack: ", stack)
        for x in range(n):
            for i in range(1,n+1):
                matrix[n-i].append(stack.pop())
                
            print ("Matrix: ", matrix)
        
                
