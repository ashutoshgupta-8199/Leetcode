class Solution(object):
    def minOperations(self, nums, x):
        if x == 0:
            return 0

        prefix_sum = {0: -1}
        right_sum = 0
        left_sum = 0
        n = len(nums)
        minmoves = float('inf')

        # Step 1: Record prefix sums and check left-only matches
        for i, num in enumerate(nums):
            left_sum += num
            if left_sum == x:
                minmoves = min(minmoves, i + 1)
            if left_sum not in prefix_sum:
                prefix_sum[left_sum] = i

        # Step 2: Iterate backward for suffix sums and match with prefix lookup
        for j in range(n - 1, -1, -1):
            right_sum += nums[j]
            needed_left = x - right_sum

            # Ensure prefix index does not overlap with suffix index j
            if needed_left in prefix_sum and prefix_sum[needed_left] < j:
                minmoves = min(minmoves, n - j + prefix_sum[needed_left] + 1)

        return minmoves if minmoves != float('inf') else -1
        