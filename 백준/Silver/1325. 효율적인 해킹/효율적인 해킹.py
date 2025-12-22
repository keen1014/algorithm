import sys
from collections import defaultdict
from collections import deque
input=sys.stdin.readline
N, M= map(int, input().strip().split())
def bfs(x):
    visited=[False]*(N+1)
    visited[x]=True
    cnt=1
    dq=deque([x])
    while dq:
        tmp=dq.popleft()
        for next in dic[tmp]:
            if not visited[next]:
                visited[next]=True
                dq.append(next)
                cnt+=1
    return cnt
dic=defaultdict(list)
for i in range(M):
    x, y=map(int, input().strip().split())
    dic[y].append(x)
max_cnt=0
answer=[]
for i in range(1, N+1):
    dfs_ans=bfs(i)
    if max_cnt<dfs_ans:
        max_cnt=dfs_ans
        answer=[i]
    elif max_cnt==dfs_ans:
        answer.append(i)
print(*answer)