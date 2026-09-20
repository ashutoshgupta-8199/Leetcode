class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        for i in range(len(s)):
            value = ord(s[i]) - ord('a') + 1
            reverse_value = 27 - value
            c += (i + 1) * reverse_value
        return c
        