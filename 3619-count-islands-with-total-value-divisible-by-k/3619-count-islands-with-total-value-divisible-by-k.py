class Solution(object):
    def countIslands(self, grid, k):
        check =[[0]*len(grid[0]) for i in range(len(grid))]
        n= len(grid)
        m= len(grid[0])
        def island_sum(i , j):
            if not (0<=i<n ) or not (0<=j<m):
                return 0 
            if grid[i][j]==0:
                return 0 
            if check[i][j]:
                return 0 
            check[i][j]= 1
            return grid[i][j]+island_sum(i+1 , j) + island_sum(i,j+1) + island_sum(i-1 ,j) + island_sum(i ,j-1)

        ans =0
        for i in range(n):
            for j in range(m):
                if not check[i][j] and grid[i][j] and island_sum(i,j)%k==0:
                    ans+=1 
        return ans 