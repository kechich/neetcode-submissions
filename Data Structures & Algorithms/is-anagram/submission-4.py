"""class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1={}
        set2={}
        if not len(s)==len(t):
            return False
        for i in range(0,len(s)):
            set1[s[i]]=set1.get(s[i],0)+1
            set2[t[i]]=set2.get(t[i],0)+1
        return set1==set2"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
            

