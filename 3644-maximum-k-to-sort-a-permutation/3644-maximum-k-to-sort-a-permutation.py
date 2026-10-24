class Solution(object):
    def sortPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        andValue = (1 << 31) - 1
        flag = True

        for i in range(n):
            if nums[i] != i:
                flag = False
                andValue &= i

        if flag:
            return 0

        return andValue