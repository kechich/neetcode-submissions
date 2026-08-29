class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett=set(nums)
        res=0
        for n in nums:
            l=0
            if not n-1 in sett:
                while n+l in sett:
                    l+=1
                res=max(res,l)
            else:
                continue
        return res
                    
