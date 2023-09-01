class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        
        map = {}
        starts = []
        
        
        def dfs (row,col,word):
            if len(word) == 0:
                return True
            
            if board[row][col] == word[0]:
                map[(row,col)] = word[0]
                
                if len(word) == 1:return True
            
            
            #go right, down, left, up
            if col+1 < n and (row,col+1) not in map and board[row][col+1] == word[1]:
                res = dfs(row,col+1,word[1:])
                if res == True:
                    return res
            if row+1 < m and (row+1,col) not in map and board[row+1][col] == word[1]:
                    res = dfs(row+1,col,word[1:])
                    if res == True:
                        return res
            if col-1 >= 0 and (row,col-1) not in map and board[row][col-1] == word[1]:
                res = dfs(row,col-1,word[1:])
                if res == True:
                    return res
            if row-1 >= 0 and (row-1,col) not in map and board[row-1][col] == word[1]:
                res =  dfs(row-1,col,word[1:])
                if res == True:
                    return res
            
            del map[row,col]
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append([i,j])
        
        for coords in starts:
            if(dfs(coords[0],coords[1],word) == True):
                return True
            else:
                map = {}
                continue
        
        
        return False
                