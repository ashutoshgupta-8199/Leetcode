class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        squared = [x**2 for x in nums]
        sorted_nums = sorted(squared)
        len_neg = len(nums)//2
        len_pos = len(nums) - len_neg
        
        pos = sorted_nums[-len_pos:]
        neg = sorted_nums[:len_neg]
        
        
        return sum(pos)-sum(neg)
        