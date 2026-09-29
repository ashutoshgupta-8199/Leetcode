class Solution(object):

    def minOperations(self, nums, x):
        """
        :type nums: List[int]
        :type x: int
        :rtype: int
        """

        total = sum(nums)
        target = total - x

        right = 0
        left = 0
        longest = -1
        curr = 0

        for right in range(len(nums)):
            curr += nums[right]

            while curr > target and left <= right:
                curr -= nums[left]
                left += 1

            if curr == target:
                longest = max(longest, right - left + 1)

        if longest == -1:
            return -1

        return len(nums) - longest
        