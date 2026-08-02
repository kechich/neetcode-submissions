class Solution:

    def encode(self, strs: List[str]) -> str:
        p1,p2='',''

        for s in strs:
            p1+=str(len(s))+','
            p2+=s
        
        res=p1+'#'+p2
        return res
            


    def decode(self, s: str) -> List[str]:
        i=0
        lens=[]
        while s[i]!="#":
            l=''
            while s[i]!=',':
                l+=s[i]
                i+=1
            lens.append(int(l))
            i+=1
        i+=1
        res=[]
        for l in lens:
            res.append( s[i: i+l] )
            i+=l
        return res


            
            
            