class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        
        for i in range(1,n+1):
            j = i
            
            while j > 0:
                if(j%2 == 1):
                    ans[i] += 1 
                j //= 2
        return ans
        