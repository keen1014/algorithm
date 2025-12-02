class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        y=len(grid)
        x=len(grid[0])
        result_grid=[]
 
        for i in range(y-k+1):
            row_results=[]
            for j in range(x-k+1):
                if y<i+k or x<j+k:
                    continue
                li=[]
                for ii in range(i,i+k):
                    for jj in range(j,j+k):
                        li.append(grid[ii][jj])
                li=list(set(li))
                li.sort()
                min_val=float('inf')
                if len(li)==1:
                    min_val=0
                for idx in range(len(li)-1):
                    diff=abs(li[idx+1]-li[idx])
                    if diff < min_val:
                        min_val=diff
                row_results.append(min_val)
            result_grid.append(row_results)
        return result_grid