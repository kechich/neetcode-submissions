class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freqs=dict()
        freqt=dict()
        for i in range(len(s)):
            freqs[s[i]]=freqs.get(s[i],0)+1
            freqt[t[i]]=freqt.get(t[i],0)+1
        return freqs==freqt


            

