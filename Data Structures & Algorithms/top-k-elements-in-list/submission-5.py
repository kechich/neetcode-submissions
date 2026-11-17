class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#hash map with counts elements as keys and counts as vaules
#retrieve according to most frequesnt, i could try to sort 
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        freqs=[[] for i in range(len(nums)+1)]
        for num,cnt in count.items():
            freqs[cnt].append(num)
        res=[]
        for i in range(len(freqs)-1,-1,-1):
            for num in freqs[i]:
                res.append(num)
                if len(res)==k:
                    return res
        
        




        