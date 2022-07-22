n,m=map(int,input().split())
a=set([input() for _ in range(n)])
b=set([input() for _ in range(m)])
r=list(b&a)
r.sort()
print(len(r))
for i in r:
    print(i)