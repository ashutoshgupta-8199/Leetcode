class Solution(object):
    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """
        ts = sum(nums)
        ms = float('inf')
        l = len(nums)
        start = end = 0
        cs = 0
        while end < l:
            cs+=nums[end]
            while ts - cs < x and start <= end: # If my current sum is reducing valid interval from desired value we need to release from start 
                cs-=nums[start]
                start+=1
            if ts - cs == x:
                ms=min(ms, l-(end-start+1))
            end+=1
            
        return -1 if ms == float('inf') else ms
        