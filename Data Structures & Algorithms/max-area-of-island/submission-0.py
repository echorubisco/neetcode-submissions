class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        def dfs(r,l,area):
            if r<0 or r>m-1 or l<0 or l>n-1 or grid[r][l] == 0:
                return 0
            if grid[r][l] == 1:
                area += 1
            grid[r][l] = 0
            return 1+dfs(r+1,l,area)+dfs(r-1,l,area)+dfs(r,l+1,area)+dfs(r,l-1,area)

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i,j,0))
        return res
        