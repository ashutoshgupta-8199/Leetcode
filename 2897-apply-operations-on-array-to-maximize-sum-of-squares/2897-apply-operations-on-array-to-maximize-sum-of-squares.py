class Solution(object):
    def maxSum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        MOD = 10**9 + 7
        n = len(nums)
        result = [0] * k

        for bit in range(32):
            count = sum((num >> bit) & 1 for num in nums)

            for i in range(min(count, k)):
                result[i] |= (1 << bit)

        return sum(x * x for x in result) % MOD