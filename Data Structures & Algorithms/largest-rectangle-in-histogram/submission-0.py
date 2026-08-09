class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxa=0
        stack=[]
        n=len(heights)
        for i,height in enumerate(heights):
            start=i
            while stack and height<stack[-1][0]:
                h,j=stack.pop()
                area=h*(i-j)
                maxa=max(maxa,area)
                start=j
            stack.append((height,start))

        while stack:
            h,j=stack.pop()
            area=h*(n-j)
            maxa=max(maxa,area)

        return maxa
