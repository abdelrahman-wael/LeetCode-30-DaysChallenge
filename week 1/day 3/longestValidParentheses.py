class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        len_= len(s)
        maxCount =0
#         base index
        stack.append(-1)
        for i in range(len_):
            if s[i] == "(":
                stack.append(i)
#           closing bracket 
            else:
                if stack:
                    stack.pop()
#                 valid substring check if len is bigger than the old one  
                if stack:
                    maxCount =  max(maxCount,i - stack[-1])
#              not a valid substring push i to be the new bax index 
                else:
                    stack.append(i)
           
        
        return maxCount
