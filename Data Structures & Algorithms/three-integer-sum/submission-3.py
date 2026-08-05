class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for i,n in enumerate(nums):
            l,r=i+1,len(nums)-1
            target=-n
            if i>0 and nums[i-1]==nums[i]:
                continue
            while l<r:
                if nums[l]+nums[r]<target:
                    l+=1
                elif nums[l]+nums[r]>target:
                    r-=1
                else:
                    res.append([n,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res