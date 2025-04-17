a=int(input())
def fib(n):
    if n == 1 or n == 2:
        return 1
    else: 
        return (fib(n - 1) + fib(n - 2))
def fibonacci(n):
    f=[]
    f.append(1)
    f.append(1)
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
    return f[n-1]

print(fibonacci(a), a-2)