class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            freq[n]=freq.get(n,0)+1
        
        arr=[[] for i in range(len(nums)+1)]

        for n,f in freq.items():
            arr[f].append(n)
        c=0
        res=[]
        for i in range(len(nums),0,-1):
            for n in arr[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return res


        
