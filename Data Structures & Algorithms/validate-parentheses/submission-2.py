class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={"]":"[",")":"(","}":"{"}
        for c in s:
            if stack and c in closetoopen:
                if stack[-1]==closetoopen[c]:
                    stack.pop() 
                else: 
                    return False
            else:
                stack.append(c)
        return True if not stack else False
