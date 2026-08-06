class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix,prefix=1,1
        res=[1]*len(nums)
        for i,num in enumerate(nums):
            res[i]=prefix
            prefix*=num
        for i in range(len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res
