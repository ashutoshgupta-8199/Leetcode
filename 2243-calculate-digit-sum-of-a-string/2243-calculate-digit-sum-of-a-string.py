class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        while len(s) > k:
            sb = []
            total = 0

            for i in range(len(s)):
                total += int(s[i])

                if (i + 1) % k == 0:
                    sb.append(str(total))
                    total = 0

            if len(s) % k != 0:
                sb.append(str(total))

            s = ''.join(sb)

        return s
        