class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = collections.defaultdict(list)

        for str in strs:
                hash[tuple(sorted(str))].append(str)
        
        return hash.values()
        

        
