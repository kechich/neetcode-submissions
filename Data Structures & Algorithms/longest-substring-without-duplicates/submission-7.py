class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=res=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            w=(r-l)+1
            res=max(res,w)
            seen.add(s[r])
        return res

        
        
