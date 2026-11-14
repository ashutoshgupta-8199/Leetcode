class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        n = len(nums)
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = pre[i] + nums[i]

        best = float('inf')
        for i in range(n):
            # subarray nums[i : i+size], with l <= size <= r and i+size <= n
            for size in range(l, min(r, n - i) + 1):
                s = pre[i + size] - pre[i]
                if 0 < s < best:
                    best = s

        return -1 if best == float('inf') else best