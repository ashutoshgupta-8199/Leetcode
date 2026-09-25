class Solution(object):
    def minOperations(self, nums, x):
        target = sum(nums) - x

        if target < 0: return -1      # whole array can't even reach x, over it 🚪
        if target == 0: return len(nums)  # take EVERYTHING, leave nothing 💅

        max_len = -1
        left = 0
        curr_sum = 0

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum > target and left <= right:
                curr_sum -= nums[left]   # window too fat, shrink it 🏃‍♀️
                left += 1

            if target == curr_sum:
                max_len = max(max_len, right - left + 1)

        return len(nums) - max_len if max_len != -1 else -1
        