class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
       stack=[]

       for c in tokens:
            if c =='+':
                i2,i1=stack.pop(),stack.pop()
                stack.append(i1+i2)
            elif c =='-':
                i2,i1=stack.pop(),stack.pop()
                stack.append(i1-i2)
            elif c =='*':
                i2,i1=stack.pop(),stack.pop()
                stack.append(i1*i2)
            elif c =='/':
                i2,i1=stack.pop(),stack.pop()
                stack.append(int(i1/i2))
            else:
                stack.append(int(c))
       return stack[-1]
            