class Solution(object):
    def generateParenthesis(self, n):
        res = set()

        def func(left, right, s):
            if left == right:
                if left == n:
                    res.add(s)
                    return
                else:
                    func(left + 1, right, s + "(")

            if left < n:
                func(left + 1, right, s + "(")

            if right < left:
                func(left, right + 1, s + ")")

        func(1, 0, "(")
        return list(res)
        