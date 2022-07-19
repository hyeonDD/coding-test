n=int(input())

d={i:-1 for i in range(n+1)}

def fibonacci(x):
    if x==0:
        d[x]=0
        return 0
    elif x==1:
        d[x]=1
        return 1
    elif d[x-1]!=-1:
        d[x]=d[x-1]+d[x-2]
    d[x]=fibonacci(x-1)+fibonacci(x-2)
    return d[x]
print(fibonacci(n))
