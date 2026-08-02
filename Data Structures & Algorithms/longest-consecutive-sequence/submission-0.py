class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set(nums)
        best=0
        for n in nums:
            if not (n-1 in h):
                x=n 
                seq=1
                
                while x+1 in h:
                    seq+=1
                    x+=1
                best=max(seq, best)
        return best
