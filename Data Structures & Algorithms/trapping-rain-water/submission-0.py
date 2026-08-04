class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0, len(height)-1
        trapped=0

        maxL,maxR=0,0

        while l<r:
            currL=height[l]
            currR=height[r]

            maxL=max(maxL,currL)
            maxR=max(maxR,currR)

            if maxL<maxR:
                trapped+=maxL-currL
                l+=1
            else:
                trapped+=maxR-currR
                r-=1

        return trapped
