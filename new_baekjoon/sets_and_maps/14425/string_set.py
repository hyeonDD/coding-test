n,m=map(int,input().split())
s=set([input() for _ in range(n)])
a=[input() for _ in range(m)]
a_set=set(a)
result=a_set&s
cnt=0
for i in result:    
    cnt+=a.count(i)
print(cnt)