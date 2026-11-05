class Solution(object):
    def divide(self, dividend, divisor):
        if dividend==-2147483648 and divisor==-1:
            return 2147483647
        n=((dividend<0)!=(divisor<0))
        k=divisor>0
        dividend=abs(dividend)
        divisor=abs(divisor)
        c=divisor
        i=1
        q=0
        while dividend>= divisor:
            if dividend >=c and dividend< c+c:
                dividend=dividend-c
                q+=i
                c=divisor
                i=1
            else:
                i+=i
                c+=c

        
           
        if n:
            return -q
        else:
            return q
        