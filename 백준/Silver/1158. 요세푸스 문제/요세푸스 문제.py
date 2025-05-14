import sys
input= sys.stdin.readline
n = list(map(int, input().split()))
p=[]
a=[]
t=0
for i in range(n[0]):
    p.append(i+1)

for j in range(n[0]):
    t = (t + n[1] - 1) % len(p)
    a.append(p.pop(t))
print(f"<{', '.join(map(str, a))}>")