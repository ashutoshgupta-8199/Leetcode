class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        oddCount = 0
        evenCount =1
        cur = 0
        for n in arr:
            if (cur ==0 and n%2 ==0) or (cur == 1 and n%2 ==1):
                cur = 0
            else:
                cur = 1
            if cur %2 == 0:
                res += oddCount
                res %= 10**9+7
                evenCount+=1
            else:
                res += evenCount
                res %=10**9+7
                oddCount +=1

        return res