class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count=nums.count(0)
        bigm=1
        test=True
        i=0
        res=[]

        if zero_count>1:
            return [0]*len(nums)
                
        for num in nums:
            if num!=0:
                bigm=bigm*num
        if not 0 in nums:
            for num in nums:
                res.append(int(bigm/num))
        else:
            for i in range(len(nums)):
                if nums[i]!=0:
                    res.append(0)
                else:
                    res.append(bigm)
        return res