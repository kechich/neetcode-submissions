class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs=defaultdict(int)
        for num in nums:
            freqs[num]=freqs.get(num,0)+1
        bucks=[[]for i in range (len(nums)+1)]
        for num,count in freqs.items():
            bucks[count].append(num)
        res=[]
        i=len(bucks)-1

        while i>=0:
            for b in bucks[i]:
                res.append(b)
                if len(res)==k:
                    return res
            i-=1
            
        

                
    
        
