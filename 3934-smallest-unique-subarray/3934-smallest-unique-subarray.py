class Solution(object):
    def smallestUniqueSubarray(self, nums):
        n = len(nums)

        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9
        BASE = 100003

        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)
        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)

        for i in range(n):
            h1[i + 1] = (h1[i] * BASE + nums[i]) % MOD1
            h2[i + 1] = (h2[i] * BASE + nums[i]) % MOD2

            p1[i + 1] = p1[i] * BASE % MOD1
            p2[i + 1] = p2[i] * BASE % MOD2

        def check(length):
            freq = {}

            for i in range(n - length + 1):
                a = (h1[i + length] -
                     h1[i] * p1[length]) % MOD1

                b = (h2[i + length] -
                     h2[i] * p2[length]) % MOD2

                key = a * MOD2 + b

                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left