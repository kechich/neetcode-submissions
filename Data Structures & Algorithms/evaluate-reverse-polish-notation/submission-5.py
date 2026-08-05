class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c=="+":
                newVal=stack[-1]+stack[-2]
                stack.pop()
                stack.pop()
                stack.append(newVal)
            elif c=="-":
                newVal=stack[-2]-stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newVal)
            elif c=="*":
                newVal=stack[-2]*stack[-1]
                stack.pop()
                stack.pop()
                stack.append(newVal)
            elif c=="/":
                newVal=int(stack[-2]/stack[-1])
                stack.pop()
                stack.pop()
                stack.append(newVal)
            else:
                stack.append(int(c))
        return stack[-1]
                