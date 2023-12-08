class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hash = {}
        
        for i in range(len(nums)):
            print hash.get(nums[i])
            if hash.get(nums[i]) >= 0:
                return [i,hash.get(nums[i])]
            else:
                hash[target - nums[i]] = i
        