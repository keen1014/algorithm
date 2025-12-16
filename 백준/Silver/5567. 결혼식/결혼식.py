from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
N=int(input().strip())
M=int(input().strip())
dic=defaultdict(list)
answer=0
li=[]
li1=[]
for i in range(M):
    u, v=map(int, input().strip().split())
    dic[u].append(v)
    dic[v].append(u)
for z in dic[1]:
    li.append(z)
    li1.append(z)

for j in li1:
    for tmp in dic[j]:
        li.append(tmp)
li=set(li)
if 1 in li:
    li.remove(1)
print(len(li))