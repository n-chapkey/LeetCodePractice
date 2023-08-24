class Solution:
     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
         return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])
#         n = len(matrix[0])
#         m = len(matrix)
#         area = n*m
#         res = []
#         #edge case
#         if m == 1: return matrix[0]
        
#         i= 0
#         while len(res) < area:

#             #top row
#             res.extend(matrix[i][i:n-i])
#             if len(res) == area: return res
#             print(res)
            
#             #right side
#             for row in range(1+i,m-i):
#                 res.append(matrix[row][n-1-i])
#             if len(res) == area: return res
#             print(res)  
            
#             #bottom row
#             lastRow = matrix[m-1-i][i:n-1-i].copy()
#             lastRow.reverse()
#             res.extend(lastRow)
#             if len(res) == area: return res
#             print(res)
            
#             #left side
#             for row in range(m-2-i,i,-1):
#                 res.append(matrix[row][i])
#             i +=1
            
#             print(res)
#             # if len(res) != area:
#             #     res.extend(matrix[i+1][:n-1-i])
        
        
#         return res
           
        
        
            