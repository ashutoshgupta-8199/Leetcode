class Solution(object):
    def removeOuterParentheses(self, s):
        c=-1
        st=''
        for i in range(0,len(s)):
            if s[i]=='(':
                c+=1
            elif s[i]==')':
                c-=1
            if c>=1 and s[i]=='(' and s[i+1]==')':
                st+="()"
            if c>=1 and s[i]=='(' and s[i+1]=='(':
                st+='('
            if c>=1 and s[i]==')' and s[i+1]==')':
                st+=')'

        return st
        """
        () () )( () )( () (())
        :type s: str
        :rtype: str
        """
        