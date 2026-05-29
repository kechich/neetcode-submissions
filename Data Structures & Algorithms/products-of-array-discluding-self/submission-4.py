class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[]
        pre.append(1)
        post,res=[0]*len(nums),[0]*len(nums)
        post[len(nums)-1]=1

        for i in range(1,len(nums)):
            pre.append(pre[i-1]*nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            post[i]=post[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            res[i]=post[i]*pre[i]
        return res