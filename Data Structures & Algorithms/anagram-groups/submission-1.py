class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)
        for s in strs:
            letters=[0]*26
            for c in s:
                letters[ord(c)-ord('a')]+=1
            freq[tuple(letters)].append(s)
        res=[]
        for l,ar in freq.items():
            res.append(ar)
        return res
        

            
            
