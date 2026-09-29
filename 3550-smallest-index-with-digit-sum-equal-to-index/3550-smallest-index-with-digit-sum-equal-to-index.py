class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i == self.count(nums[i]):
                return i

        return -1

    def count(self, n):
        total = 0

        while n != 0:
            total += n % 10
            n //= 10

        return total

        
        