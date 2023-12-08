class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        theSet = set()
        
        for num in nums:
            if num in theSet:
                return True
            else:
                theSet.add(num)
        
        return False