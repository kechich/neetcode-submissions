class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best,numSet=0,set(nums)
        for num in nums:
            if num-1 not in numSet:
                current=1
                while num+current in numSet:
                    current+=1
                best=max(current,best)
        return best
