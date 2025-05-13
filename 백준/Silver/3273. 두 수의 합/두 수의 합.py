import sys
input = sys.stdin.readline
_=int(input().strip())
n_list = list(map(int, input().split()))
t = int(input().strip())
count=0
waiting_for={}

for n_val in n_list:
    if waiting_for.get(n_val, 0):
        count +=1
    else:
        target = t - n_val
        waiting_for[target]= 123
print(count)