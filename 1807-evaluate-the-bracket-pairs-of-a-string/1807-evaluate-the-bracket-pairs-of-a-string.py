class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        stack1=[]
        hashmap = {}
        cpy=""
        last_index = 0
        for a,b in knowledge:
            hashmap[a]=b
        
        for i in range(len(s)):
            if s[i]=="(":
                stack1.append(i)
            elif s[i]==")":
                start_index = stack1.pop()
                keyy = s[start_index+1:i]
                value="?"
                if keyy in hashmap:
                    value = hashmap[keyy]
                    
                cpy=cpy + value
            elif len(stack1)==0 and s[i]!="(" and s[i]!=")":
                cpy=cpy+s[i]
        # print(cpy)
        return cpy

            
                
        