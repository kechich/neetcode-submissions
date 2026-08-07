class Solution:
    def trap(self, height: List[int]) -> int:
        l,r= 0, len(height)-1
        Lmax=0
        Rmax=0
        trapped=0

        while l<r:
            currL=height[l]
            currR=height[r]

            Lmax=max(Lmax, height[l])
            Rmax=max(Rmax, height[r])

            if height[l]<height[r]:
                trapped+=Lmax-height[l]
                l+=1
            else:
                trapped+=Rmax-height[r]
                r-=1
        return trapped