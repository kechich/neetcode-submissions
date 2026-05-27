class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        first=''
        scnd=''
        for s in strs:
            first+=str(len(s))+','
            scnd+=s
        res=first+"#"+scnd
        return res
    
    def decode(self, s:str)-> List[str]:
        res=[]
        i=0
        lens=[]
        while s[i]!="#":
            length=''
            while s[i]!=',':
                length+=s[i]
                i+=1
            i+=1
            lens.append(int(length))
        i+=1
        for sz in lens:
            res.append(s[i:i+sz])
            i+=sz
        return res
                

                
            
            


                
            
            

