import sys
from collections import deque
input=sys.stdin.readline
T = int(input().strip())
stack=[]
m=[]
for _ in range(T):
    m=[]
    임시=[]
    n= int(input().strip())
    cnt=n
    vis=[0 for i in range(n+1)]
    select=list(map(int, input().strip().split()))
    select=[0]+select
    for i in range(1,n+1):
        if vis[i]==0:
            stack.append(i)
            vis[i]=1
            while stack:
                top=stack[-1]
                if vis[select[top]]==0:
                    stack.append(select[top])
                    vis[select[top]]=1
                    
                elif vis[select[top]]==1:
                    tmp=select[top]
                    임시=[]
                    while stack and stack[-1] != tmp:
                        vis[stack[-1]]=2
                        임시.append(stack[-1])
                        stack.pop()
                    if stack:
                        m+=임시
                        vis[stack[-1]]=2
                        m.append(stack[-1])
                        stack.pop()
                        while stack:
                            vis[stack[-1]]=2
                            stack.pop()
                else:
                    stack=[]
                    break
    print(cnt-len(m))