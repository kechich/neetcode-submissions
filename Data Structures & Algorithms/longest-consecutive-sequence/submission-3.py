class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        res=0
        for num in nums:
            l=0
            if not num-1 in numSet:
                l+=1
                while num+l in numSet:
                    l+=1
                res=max(l,res)
            else:
                continue
        return res