class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]==0:
            return 0
        for i in range(1, len(nums)):
            if nums[i]>=10:
                n = nums[i]
                sum_d = 0
                while n>0:
                    sum_d+=n%10
                    n//=10
                if sum_d == i:
                    return i
                else:
                    continue
            if nums[i]==i:
                return i
        return -1


        
        