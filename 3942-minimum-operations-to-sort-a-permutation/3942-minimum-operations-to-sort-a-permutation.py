class Solution(object):
    def minOperations(self, nums):
        n = len(nums)
        S = sorted(nums)

        if nums == S:
            return 0

        # nums == L^k(T)  k return, not None
        def get_k(T):
            pos = {v: i for i, v in enumerate(T)}
            if nums[0] not in pos:
                return None
            k = pos[nums[0]]
            for i in range(n):
                if nums[i] != T[(i + k) % n]:
                    return None
            return k

        ans = float("inf")

        # State 1: nums, sorted arrays rotation
        k = get_k(S)
        if k is not None:
            # nums = L^k(S)  order for needed L^(n-k) 
            a = (n - k) % n
            # L^a cost:
            # a times L  or (n-a) times L + 2 times  R
            ans = min(ans, min(a, n - a + 2))

        # State 2: nums, reversed sorted arr rotation 
        k = get_k(S[::-1])
        if k is not None:
            # nums =  if L^k(R(S))  cost = 1 + min(k, n-k)
            ans = min(ans, 1 + min(k, n - k))

        return -1 if ans == float("inf") else ans