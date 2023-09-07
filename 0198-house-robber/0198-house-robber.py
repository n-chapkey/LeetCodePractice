class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = {}
        one = nums[-1]
        two = 0
        for i in range(len(nums)-2,-1,-1):
            temp = nums[i] + two
            
            two = one
            one = max(temp,one)
            
        return one