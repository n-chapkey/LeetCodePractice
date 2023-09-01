class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r = 0,len(height)-1
        width = r-l
        maxArea = min(height[l],height[r])*width

        while l != r:
            if height[l]<=height[r]:
                l += 1
            else:
                r -=1
            currArea = min(height[l],height[r])*(r-l)
            maxArea = max(maxArea,currArea)
        
        return maxArea