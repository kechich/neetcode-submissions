class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdir,tdir={},{}
        if len(s)!=len(t):
            return False
        for c in s:
            sdir[c]=sdir.get(c,0)+1
        for c in t:
            tdir[c]=tdir.get(c,0)+1
        return sdir==tdir

            