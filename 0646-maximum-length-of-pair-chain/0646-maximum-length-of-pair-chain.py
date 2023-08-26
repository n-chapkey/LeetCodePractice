class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        
        if len(pairs) == 1:
            return 1

        sortedPairs = sorted(pairs,key=lambda x:x[1])
        longest = 1
        current = 1
        lastPair = sortedPairs[0]
        
        
        for i in sortedPairs[1:]:
            if lastPair[1] < i[0]:
                lastPair = i
                current += 1
                longest = max(current,longest)
            
        
        
        return longest