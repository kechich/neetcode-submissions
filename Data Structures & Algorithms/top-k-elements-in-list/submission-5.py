class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for num in nums:
            count[num]=count.get(num,0)+1
        array=[]
        for num,cnt in count.items():
            array.append([cnt,num])
        array.sort()
        res=[0]*k
        for i in range (k):
            res[i]=array.pop()[1]
        return res
        
