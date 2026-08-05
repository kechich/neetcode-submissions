class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)

        for i,t in enumerate(temperatures):
            
            while stack and t>stack[-1][1]:
                pre_i,pre_t=stack.pop()
                res[pre_i]=i-pre_i
                
            stack.append((i,t))
        return res