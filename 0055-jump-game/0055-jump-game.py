class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = len(nums)-1
        arr = nums.copy()
        res = False
        DP = []

        
        
        for ind in range(len(nums)-1,-1,-1):
            if(r == 0):
                return True
            else:
                if (r-ind <= nums[ind]):
                    r = ind
                    if r == 0:
                        return True
                    
        return False