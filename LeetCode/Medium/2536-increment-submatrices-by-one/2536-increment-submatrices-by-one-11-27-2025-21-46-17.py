class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        answer=[[0 for i in range(n+1)] for j in range(n+1)]
        for i in range(len(queries)):
            y1, x1, y2, x2=queries[i]
            answer[y1][x1]+=1
            answer[y2+1][x1]-=1
            answer[y1][x2+1]-=1
            answer[y2+1][x2+1]+=1
        for i in range(n):
            for j in range(1,n):
                answer[i][j]+=answer[i][j-1]
        for i in range(1,n):
            for j in range(n):
                answer[i][j]+=answer[i-1][j]
        return [i[:n] for i in answer[:n]]