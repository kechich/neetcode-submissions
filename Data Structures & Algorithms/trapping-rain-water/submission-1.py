class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        maxL,maxR=0,0
        trapped=0

        while l<r:

            currL,currR=height[l],height[r]

            maxL=max(currL,maxL)
            maxR=max(currR,maxR)

            if maxL<maxR:
                trapped+=maxL-currL
                l+=1
            else:
                trapped+=maxR-currR
                r-=1
        return trapped
            