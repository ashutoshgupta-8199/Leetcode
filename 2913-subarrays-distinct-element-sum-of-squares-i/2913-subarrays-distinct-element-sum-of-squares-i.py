class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0

        for i in range(n):
            st = set()

            for j in range(i, n):
                st.add(nums[j])
                m = len(st)
                res += m * m

        return res
        