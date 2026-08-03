class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j,nums,res=0,len(numbers)-1,sorted(numbers),[]
        while i<j:
            if nums[i]+nums[j]<target:
                i+=1
            if nums[i]+nums[j]>target:
                j-=1
            if nums[i]+nums[j]==target:
                break
        return [i+1,j+1]
        
            
