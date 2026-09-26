class Solution(object):
    def smallestIndex(self, nums):
        n = len(nums)

        for i in range(n):
            sum = 0
            num = nums[i]

            while num > 0:
                sum += num % 10
                num //= 10

            if sum == i:
                return i

        return -1
        


        
        