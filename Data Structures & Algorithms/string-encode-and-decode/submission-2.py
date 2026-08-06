class Solution:

    def encode(self, strs: List[str]) -> str:
        p1,p2='',''
        for s in strs:
            p1+=str(len(s))+','
            p2+=s
        res= p1+"#"+p2
        return res

    def decode(self, s: str) -> List[str]:
       lens=[]
       i=0
       while not s[i]=="#":
            l=''
            while not s[i]==',':
                l+=s[i]
                i+=1
            lens.append(int(l))
            i+=1
       i+=1
       res=[]
       for n in lens:
            res.append(s[i:i+n])
            i+=n
        
       return res



            
            
            