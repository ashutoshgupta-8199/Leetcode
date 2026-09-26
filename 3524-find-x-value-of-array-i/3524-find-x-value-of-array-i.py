class Solution(object):
    def resultArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = [0] * k
        current = [0] * k

        for num in nums:
            next_count = [0] * k

            next_count[num % k] += 1

            for r in range(k):
                new_remainder = (r * num) % k
                next_count[new_remainder] += current[r]

            current = next_count

            for r in range(k):
                result[r] += current[r]

        return result