class Solution(object):
    def maxSelectedElements(self, nums):
        nums.sort()
        dp = {}
        max_len = 0

        for x in nums:
            v1 = dp.get(x, 0) + 1
            v2 = dp.get(x - 1, 0) + 1

            if dp.get(x + 1, 0) < v1:
                dp[x + 1] = v1
            if dp.get(x, 0) < v2:
                dp[x] = v2

            if dp[x + 1] > max_len:
                max_len = dp[x + 1]
            if dp[x] > max_len:
                max_len = dp[x]

        return max_len