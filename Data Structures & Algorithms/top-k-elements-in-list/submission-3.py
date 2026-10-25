class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        freqs=[[] for i in range(len(nums)+1)]
        for n,c in count.items():
            freqs[c].append(n)
        res=[]
        for i in range(len(freqs)-1,-1,-1):
            for n in freqs[i]:
                res.append(n)
                
                if len(res)==k:
                    return res
        return []




        