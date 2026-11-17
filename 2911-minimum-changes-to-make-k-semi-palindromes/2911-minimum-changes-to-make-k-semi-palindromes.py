class Solution(object):
    def minimumChanges(self, s, k):
        n = len(s)
        INF = 10**9

        divisors = [[] for _ in range(n + 1)]

        for d in range(1, n):
            for length in range(2 * d, n + 1, d):
                divisors[length].append(d)

        cost = [[INF] * n for _ in range(n)]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for d in divisors[length]:
                    changes = 0

                    for r in range(d):
                        left = i + r
                        right = i + r + (length // d - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    cost[i][j] = min(cost[i][j], changes)

        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    if dp[p - 1][j] != INF:
                        dp[p][i] = min(
                            dp[p][i],
                            dp[p - 1][j] + cost[j][i - 1]
                        )

        return dp[k][n]