class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped=defaultdict(list)
        for s in strs:
            freq=[0]*26
            for c in s:
                freq[ord(c)-ord('a')]+=1
            grouped[tuple(freq)].append(s)
        res=[]
        for freq,arr in grouped.items():
            res.append(arr)
        
        return res