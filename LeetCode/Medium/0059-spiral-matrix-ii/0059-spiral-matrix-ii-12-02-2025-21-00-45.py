class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix=[[0]*n for i in range(n)]
        dx=[1, 0, -1, 0]
        dy=[0, 1, 0, -1]
        x=0
        y=0
        direction=0 #0 오른, 1 아래, 2 왼, 3 위
        for num in range(1, n*n+1):
            matrix[y][x]=num
            ny=y+dy[direction]
            nx=x+dx[direction]
            
            if not (0<=ny<n and 0<=nx<n and matrix[ny][nx]==0):
                direction=(direction+1)%4
                ny=y+dy[direction]
                nx=x+dx[direction]
            y=ny
            x=nx
        return matrix
