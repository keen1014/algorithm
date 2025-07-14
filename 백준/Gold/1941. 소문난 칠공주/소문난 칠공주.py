import sys
input=sys.stdin.readline
cnt=0
def princess7(N,S,Y,start):
    global cnt
    if N==7 and 4<=S:
        if BFS(li):
            cnt+=1
        return
    elif N==7 and S<4 or 3<Y:
        return

    for i in range(start, 25):
        y,x=divmod(i,5)
        if not vis[i]:
            vis[i]=True
            li[N]=(y,x)
            if sy_dict[(y,x)]=='S':
                princess7(N+1,S+1,Y,i+1)
            elif sy_dict[(y,x)]=='Y':
                princess7(N+1,S,Y+1,i+1)
            vis[i]=False

            
def BFS(list):
    s=set(list)
    if len(s)<=6:
        return False
    a=s.pop()
    queue=[a]
    while queue:
        y,x=queue.pop()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if (ny, nx) in s:
                queue.append((ny,nx))
                s.remove((ny,nx))
    if s:
        return False
    return True

dx=[0, -1, 0, 1]
dy=[-1, 0, 1, 0]
vis=[False]*25
li=[(0,0)]*7
sy_dict={}
for i in range(5):
    line=list(input().strip())
    for j in range(5):
        sy_dict[(i,j)]=line[j]
princess7(0,0,0,0)
print(cnt)