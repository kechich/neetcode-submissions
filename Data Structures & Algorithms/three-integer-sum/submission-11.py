class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        numbers=sorted(nums)
        for i,a in enumerate(numbers):
            if i>0 and a==numbers[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                threesome=a+numbers[l]+numbers[r]
                if threesome>0:
                    r-=1
                elif threesome<0:
                    l+=1
                else:
                    res.append([numbers[l],numbers[r],a])
                    l+=1
                    r-=1
                    while numbers[l]==numbers[l-1] and l<r:
                        l+=1

        return res
