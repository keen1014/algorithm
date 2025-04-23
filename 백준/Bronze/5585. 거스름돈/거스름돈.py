a=int(input())
b=1000-a
c= b/500
b=b%500
d= b/100
b= b%100
e= b/50
b = b%50
f= b/10
b = b%10
g= b/5
b = b%5
# print(b, int(c), int(d), int(e), int(f), int(g))
print(int(b)+int(c)+int(d)+int(e)+int(f) +int(g))