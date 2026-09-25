class Solution:
    def longestCommonPrefix(self, strs):

        minLen = min(len(word) for word in strs)

        prefix = ""

        for pos in range(minLen):

            current = strs[0][pos]

            for i in range(1, len(strs)):
                if strs[i][pos] != current:
                    return prefix

            prefix += current

        return prefix