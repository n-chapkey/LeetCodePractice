class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        intervals.append(newInterval)
        sortedInts = sorted(intervals, key=lambda i:i[0])
        out = []
        
        for i in sortedInts:
            if out and  i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1],i[1])
            else:
                out += [i]
        return out        