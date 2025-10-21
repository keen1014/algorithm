class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        
        for i in range(n):
            if 0==grid[i][i] or grid[i][n-i-1] ==0:
                return False
            for j in range(n):
                if (n-i-1)== j and 0!=grid[i][i] and grid[i][n-i-1] !=0:
                    continue
                elif i!= j and grid[i][j]!=0:
                    return False
        return True