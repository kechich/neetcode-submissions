class Solution:

    def encode(self, strs: List[str]) -> str:
        
        frst=""
        scnd=""
        for s in strs:
            frst+=str(len(s))+","
            scnd+=s
        return frst+"#"+scnd
    
    def decode(self, s:str)-> List[str]:
        sizes=[]
        i=0
        while s[i]!='#':
            sz=""
            while s[i]!=",":
                sz+=s[i]
                i+=1
            sizes.append(int(sz))
            i+=1
        i+=1
        res=[]
        for sz in sizes:
            res.append(s[i:i+sz])
            i+=sz
        return res



                
            
            


                
            
            

