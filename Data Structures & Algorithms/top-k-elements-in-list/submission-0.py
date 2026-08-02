class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        bucks=[[]for i in range(len(nums)+1)]
        for num,fr in freq.items():
            bucks[fr].append(num)
        
        res=[]
        
        for i in range(len(bucks)-1,0,-1):
            for num in bucks[i]:
                res.append(num)
                if len(res)==k:
                    return res
                
