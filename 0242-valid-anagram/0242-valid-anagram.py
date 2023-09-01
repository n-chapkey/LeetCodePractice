class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sArr = list(s)
        sArr.sort()
        s = "".join(sArr)
        
        tArr = list(t)
        tArr.sort()
        t = "".join(tArr)

        return s == t