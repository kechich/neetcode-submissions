class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        res=[]
        for i,num in enumerate(nums):
            diff=target-num
            if not num in seen:
                seen[num]=i
            if diff in seen:
                res=[seen[diff],i]
        return res
