class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for s in strs:
            occ=[0]*26
            for c in s:
                occ[ord(c)-ord("a")]+=1
            group[tuple(occ)].append(s)
        
        return list(group.values())


            
            
