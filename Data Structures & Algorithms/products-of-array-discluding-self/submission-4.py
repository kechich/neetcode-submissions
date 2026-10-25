class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        pre=1
        for i in range(1,len(nums),1):
            res[i]=nums[i-1]*pre
            pre*=nums[i-1]
        post=1
        for i in range(len(nums)-2,-1,-1):
            res[i]*=nums[i+1]*post
            post*=nums[i+1]
        
        return res
