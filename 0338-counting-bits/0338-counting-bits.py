class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        nextSigBit = 1
        sigBit = 0
            
        if n == 1:
            return [0,1]
        
        for i in range(1,n+1):
            if i == nextSigBit:
                sigBit = nextSigBit
                nextSigBit *=2
            ans[i] = 1 + ans[i-sigBit]
                
            

                

        return ans
        