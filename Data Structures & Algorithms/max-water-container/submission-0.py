class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        best=min(heights[l],heights[r])*(r-l)
        while l<r:
            if min(heights[l],heights[r])==heights[r]:
                r-=1
            elif min(heights[l],heights[r])==heights[l]:
                l+=1
            best=max(min(heights[l],heights[r])*(r-l),best)
        return best