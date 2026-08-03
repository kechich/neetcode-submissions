class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers=sorted(nums)
        res=[]
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i - 1]:
                continue
            t=0-numbers[i]
            l,r=i+1,len(numbers)-1
            while l<r:
                if numbers[l]+numbers[r]<t:
                    l+=1
                elif numbers[l]+numbers[r]>t:
                    r-=1
                else:
                    res.append([numbers[i],numbers[l],numbers[r]])
                    l += 1
                    r -= 1
                    while l < r and numbers[l] == numbers[l - 1]:
                        l += 1
                    while l < r and numbers[r] == numbers[r + 1]:
                        r -= 1
        return res

            
