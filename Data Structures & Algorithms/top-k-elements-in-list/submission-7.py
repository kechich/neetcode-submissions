class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[]for i in range(len(nums)+1)]

        for num in nums:
            count[num]=count.get(num,0)+1
        """array=[]
        for num,cnt in count.items():
            array.append([cnt,num])
        array.sort()
        res=[0]*k
        for i in range (k):
            res[i]=array.pop()[1]
        return res"""
        for num,cnt in count.items():
            freq[cnt].append(num)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res       
        
