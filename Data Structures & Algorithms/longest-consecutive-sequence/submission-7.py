class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        l=0
        maxl=0
        lis=set(nums)

        for n in nums:
            if n-1 in lis:
                continue
            else:
                l+=1
                while n+l in lis:
                    l+=1
                maxl=max(l,maxl)
                l=0
        return maxl