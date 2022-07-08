import sys

n = int(sys.stdin.readline())

cnt = {'cnt':0}

def fib(n):
    if n==1 or n==2:
        cnt['cnt'] += 1
        return 1
    else:
        return (fib(n - 1) + fib(n - 2))

d = {0:0,1:1,2:1}

cnt2 = {'cnt2':0}
def fibonacci(n):
    for i in range(3,n+1):
        cnt2['cnt2'] += 1
        d[i] = d[i-1] + d[i-2]
    return d[n]

fib(n)
fibonacci(n)

print(cnt['cnt'],cnt2['cnt2'])
