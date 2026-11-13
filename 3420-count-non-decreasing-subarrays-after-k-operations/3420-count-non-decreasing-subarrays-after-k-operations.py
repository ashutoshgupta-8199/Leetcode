class Solution(object):
    def countNonDecreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        a = nums[::-1]
        n = len(a)
        dq = [0] * n          # monotonic stack/queue of indices; active part is dq[head:tail]
        head = tail = 0
        l = 0
        cost = 0
        ans = 0

        for r in range(n):
            x = a[r]
            # a[r] becomes the suffix max for every popped segment
            while tail > head and a[dq[tail - 1]] <= x:
                tail -= 1
                j = dq[tail]
                prev = dq[tail - 1] if tail > head else l - 1
                cost += (x - a[j]) * (j - prev)
            dq[tail] = r
            tail += 1

            # shrink from the left until the cost fits within k
            while cost > k:
                cost -= a[dq[head]] - a[l]
                if dq[head] == l:
                    head += 1
                l += 1

            ans += r - l + 1

        return ans
        