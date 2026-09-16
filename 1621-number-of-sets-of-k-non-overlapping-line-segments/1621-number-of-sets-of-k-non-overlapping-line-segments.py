class Solution(object):
    def numberOfSets(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        modulo = 10**9 + 7
        dp = [[0] * (k+1) for _ in range(n+1)]
        v_b_list = [0] * (k+1)
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(2, n+1):
            for j in range(1, k+1):
                v_b_list[j] = v_b_list[j] + dp[i-1][j-1]
                v_a = dp[i-1][j]
                dp[i][j] = v_a + v_b_list[j]
        return dp[n][k] % modulo
        