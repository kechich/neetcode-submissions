class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new=defaultdict(list)
        for el in strs:
            letter=[0]*26
            for char in el:
                letter[ord(char)-ord("a")]+=1
            
            new[tuple(letter)].append(el)
            
        
        return list(new.values())



            
            
