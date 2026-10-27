class Solution(object):
    def createGrid(self, m, n):
        arr = [["#" for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == n - 1:
                    arr[i][j] = "."

        for i in range(m):
            arr[i] = "".join(arr[i])

        return arr