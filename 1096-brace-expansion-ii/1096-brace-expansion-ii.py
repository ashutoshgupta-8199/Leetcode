class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        stack = []
        union = []
        prod = [""]
        
        for c in expression:
            if c.isalpha():
                
                prod = [s + c for s in prod]
                
            elif c == '{':
                
                stack.append(union)
                stack.append(prod)
                union, prod = [], [""]
                
            elif c == '}':
                
                prev_prod = stack.pop()
                prev_union = stack.pop()
                
                curr_inner_words = union + prod
                
                prod = [p + w for p in prev_prod for w in curr_inner_words]
                union = prev_union
                
            elif c == ',':
                
                union += prod
                prod = [""]
                
       
        return sorted(list(set(union + prod)))
        