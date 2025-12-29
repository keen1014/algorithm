import sys
from collections import deque
input=sys.stdin.readline
K=int(input().strip())
for _ in range(K):
    dic={}
    V, E=map(int, input().split())
    visited=[0]*(V+1)
    for i in range(1,V+1):
        dic[i]=list()
    for i in range(E):
        u, v =map(int, input().split())
        dic[u].append(v)
        dic[v].append(u)

    answer=True
    for i in range(1, V+1):
        if answer == False:
            break
        if visited[i] == 0:
            dq=deque([i])
            visited[i]=1
            
        while dq:
            tmp=dq.popleft()
            for neighbor in dic[tmp]:
                if visited[neighbor] == 0:
                    visited[neighbor]=-visited[tmp]
                    dq.append(neighbor)
                elif visited[neighbor] == visited[tmp]:
                    answer=False
                    break
            if answer==False:
                break
    print("YES" if answer else "NO")