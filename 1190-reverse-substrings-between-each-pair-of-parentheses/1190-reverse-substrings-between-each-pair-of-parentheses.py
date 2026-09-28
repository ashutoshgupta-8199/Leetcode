class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result=""
        stack=[]
        n=len(s)
        for i in range(n):
            # print "stack is:", stack
            if s[i]==")":
                pop=""
                j=len(stack)-1
                while stack[j]!="(":
                    pop+=stack[j]
                    stack.pop()
                    j-=1
                stack.pop()
                # print("inside pop is:",pop)
                pop=pop[::-1]
                if "(" not in stack:
                    stack.append(pop[::-1])
                else:
                    stack.append(pop)
            else:
                stack.append(s[i])
        # print("final stack is:",stack)
        for i in stack:
            result+=i
        return result