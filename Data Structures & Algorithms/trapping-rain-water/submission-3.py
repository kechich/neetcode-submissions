class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        Lmax,Rmax=0,0

        trapped=0
        
        while l<r:

            Lmax=max(height[l],Lmax)
            Rmax=max(height[r],Rmax)

            if Lmax<Rmax:
                trapped+=Lmax-height[l]
                l+=1
            else:
                trapped+=Rmax-height[r]
                r-=1
        return trapped