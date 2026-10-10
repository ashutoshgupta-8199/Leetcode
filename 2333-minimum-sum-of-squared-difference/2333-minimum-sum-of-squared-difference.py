class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k1: int
        :type k2: int
        :rtype: int
        """
        k = k1 + k2
        diffs = [abs(x - y) for x, y in zip(nums1, nums2)]
        
        if sum(diffs) <= k:
            return 0
        
        max_diff = max(diffs)
        buckets = [0] * (max_diff + 1)
        
        for d in diffs:
            buckets[d] += 1
            
        for i in range(max_diff, 0, -1):
            if k == 0:
                break
            count = buckets[i]
            if count > 0:
                if k >= count:
                    buckets[i] = 0
                    buckets[i - 1] += count
                    k -= count
                else:
                    buckets[i] -= k
                    buckets[i - 1] += k
                    k = 0
        
        ans = 0
        for val, count in enumerate(buckets):
            if count > 0:
                ans += count * (val * val)
                
        return ans
        